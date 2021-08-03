class Solution:
    def countVowelPermutation(self, n: int) -> int:
        last = [1] * 5
        MOD = 1e9 + 7
        for i in range(1, n):
            tempLast = [0] * 5
            tempLast[0] = (last[1] + last[2] + last[4]) % MOD
            tempLast[1] = (last[0] + last[2]) % MOD
            tempLast[2] = (last[1] + last[3]) % MOD
            tempLast[3] = (last[2]) % MOD
            tempLast[4] = (last[3] + last[2]) % MOD
            last = tempLast
        return int(sum(last) % MOD)
