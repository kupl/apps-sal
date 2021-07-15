class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        length = [0] * (len(arr) + 2)
        res = -1
        
        for i, pos in enumerate(arr):
            left, right = length[pos - 1], length[pos + 1]
            if left == m or right == m:
                res = i
            length[pos - left], length[pos + right] = left + right + 1, left + right + 1
            
        return res
