class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m 
        groups = [0] * (len(arr) + 2)
        res = -1
        for i, num in enumerate(arr):
            left, right = groups[num - 1], groups[num + 1]
            groups[num-groups[num-1]] = left + right + 1
            groups[num+groups[num+1]] = left + right + 1
            if left == m or right == m :
                res = i
        return res

