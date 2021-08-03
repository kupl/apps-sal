class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        begins = [-1] * (K + 1)
        cur = [0] * (K + 1)
        maxL = 0
        curMax = 0
        for i, a in enumerate(A):
            if a == 0:
                maxL = max(maxL, curMax)
                begins.pop(0)
                begins.append(i)
                curMax -= cur.pop(0)
                curMax += 1 if begins[0] == -1 else 0
                cur.append(0)
            else:
                cur[-1] += 1
                curMax += 1
        return max(maxL, curMax)
