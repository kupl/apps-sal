class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0 for i in range(len(arr) + 2)]
        count = [0 for i in range(len(arr) + 1)]
        res = -1
        for i, v in enumerate(arr):
            left, right = length[v - 1], length[v + 1]
            length[v] = left + right + 1
            length[v - left] = left + right + 1
            length[v + right] = left + right + 1
            if count[left] > 0:
                count[left] -= 1
            if count[right] > 0:
                count[right] -= 1
            count[length[v]] += 1
            if count[m]:
                res = i + 1
        return res
