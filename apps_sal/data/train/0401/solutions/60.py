class Solution:
    def maxSumDivThree(self, A):
        print(A)
        seen = [0, 0, 0]
        for a in A:
            temp = seen.copy()
            for i in seen:            
                temp[(i + a) % 3] = max(temp[(i + a) % 3], i + a)
            seen = temp

        return seen[0]
