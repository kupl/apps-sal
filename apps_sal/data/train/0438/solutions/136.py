class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        count = [0] * (len(arr)+1)
        length = [0] * (len(arr)+2)
        res = -1
        for i, n in enumerate(arr):
            left, right = length[n-1], length[n+1]
            length[n] = length[n-left] = length[n+right] = left+right+1
            count[left] -= 1
            count[right] -= 1
            count[left+right+1] += 1
            if count[m] > 0:
                res = i + 1
        return res
