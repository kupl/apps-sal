class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        count = [1, 0]
        cur = answer = 0
        for n in arr:
            cur ^= n & 1
            answer = (answer + count[1 ^ cur]) % MOD
            count[cur] += 1
        return answer
