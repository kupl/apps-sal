class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for step, i in enumerate(arr):
            left, right = length[i - 1], length[i + 1]
            length[i] = length[i - left] = length[i + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[i]] += 1
            if count[m]:
                res = step + 1
        return res
