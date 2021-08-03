class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7

        def memo(f):
            dic = {}

            def f_alt(*args):
                if args not in dic:
                    dic[args] = f(*args)
                return dic[args]
            return f_alt

        @memo
        def find_answer(n, l):
            if n == 1:
                return 1
            if n <= 0:
                return 0
            return (find(n - 1) - (find(n - rollMax[l] - 1) - find_answer(n - rollMax[l] - 1, l))) % mod

        @memo
        def find(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return sum(find_answer(n, r) for r in range(6)) % mod

        return find(n)
