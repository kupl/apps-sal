class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        ans = 0
        for step, index in enumerate(arr):
            left = length[index - 1]
            right = length[index + 1]
            length[index - left] = length[index + right] = right + left + 1
            count[left] -= 1
            count[right] -= 1
            count[right + left + 1] += 1
            if count[m] > 0:
                ans = step + 1
        if ans == 0:
            return -1
        return ans
