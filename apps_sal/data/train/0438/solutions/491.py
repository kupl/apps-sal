class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        size = [0] * (n + 2)
        size_count = [0] * (n + 1)
        res = -1
        for (step, num) in enumerate(arr):
            (left, right) = (size[num - 1], size[num + 1])
            size[num] = size[num - left] = size[num + right] = left + right + 1
            size_count[left] -= 1
            size_count[right] -= 1
            size_count[size[num]] += 1
            if size_count[m]:
                res = max(res, step + 1)
        return res
