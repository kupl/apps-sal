class Solution:
    def numOfSubarrays(self, A):
        count = [1, 0]
        curr = res = 0
        for a in A:
            curr ^= a & 1
            res += count[1 - curr]
            count[curr] += 1
        return res % (10 ** 9 + 7)
