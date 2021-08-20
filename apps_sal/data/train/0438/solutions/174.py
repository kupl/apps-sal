class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        count = [0] * (len(arr) + 2)
        length = [0] * (len(arr) + 2)
        ans = -1
        for (i, a) in enumerate(arr):
            (left, right) = (length[a - 1], length[a + 1])
            length[a] = left + right + 1
            length[a - left] = length[a]
            length[a + right] = length[a]
            count[left] -= 1
            count[right] -= 1
            count[left + right + 1] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
