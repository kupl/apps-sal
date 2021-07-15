class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        d = {
            0: (1,),
            1: (0, 2),
            2: (0, 1, 3, 4),
            3: (2, 4),
            4: (0,)
        }
        a0 = [1] * 5
        for i in range(n - 1):
            a1 = [0] * 5
            for j in range(5):
                for k in d[j]:
                    a1[k] = (a1[k] + a0[j]) % mod
            a0 = a1
        return sum(a0) % mod
