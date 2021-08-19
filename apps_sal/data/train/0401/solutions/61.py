class Solution:

    def maxSumDivThree(self, A):
        seen = [0, 0, 0]
        for a in A:
            for i in seen:
                temp = seen.copy()
                temp[(i + a) % 3] = max(temp[(i + a) % 3], i + a)
                seen = temp
        return seen[0]
