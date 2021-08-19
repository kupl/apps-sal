class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def recursion(n, last, freq):
            if n == 0:
                return 1
            answer = 0
            for i in range(6):
                if i == last:
                    if freq == rollMax[i]:
                        continue
                    else:
                        answer += recursion(n - 1, last, freq + 1)
                else:
                    answer += recursion(n - 1, i, 1)
            return answer
        return recursion(n, -1, 0) % (10 ** 9 + 7)
