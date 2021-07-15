class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        cnt = [0] * (len(arr) + 1)
        res = -1
        for i, num in enumerate(arr):
            left, right = length[num - 1], length[num + 1]
            length[num] = length[num - left] = length[num + right] = left + right + 1
            cnt[length[num]] += 1
            cnt[left] -= 1
            cnt[right] -= 1
            if cnt[m] > 0:
                res = i + 1
        return res
