class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (length, count) = ([0 for i in range(len(arr) + 2)], [0 for i in range(len(arr) + 2)])
        ans = -1
        for (i, num) in enumerate(arr):
            (left, right) = (length[num - 1], length[num + 1])
            (length[num - left], length[num + right]) = (left + right + 1, left + right + 1)
            count[left] -= 1
            count[right] -= 1
            count[left + right + 1] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
