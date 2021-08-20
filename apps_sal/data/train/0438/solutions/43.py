class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        ret = -1
        n = len(arr)
        length = [0] * (n + 2)
        count = [0] * (n + 1)
        for i in range(n):
            a = arr[i]
            left = length[a - 1]
            right = length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m] > 0:
                ret = i + 1
        return ret
