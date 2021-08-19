class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res, n = -1, len(arr)
        # length of group
        length = [0] * (n + 2)
        # count of length
        count = [n] + [0] * n

        for i, v in enumerate(arr):
            left, right = length[v - 1], length[v + 1]
            length[v] = length[v - left] = length[v + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[v]] += 1
            if count[m]:
                res = i + 1
        return res
