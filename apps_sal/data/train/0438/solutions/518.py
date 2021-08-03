class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        res = -1
        length = [0] * (n + 2)
        count = [0] * (n + 1)
        for i in range(n):
            b = arr[i]

            left, right = length[b - 1], length[b + 1]

            length[b] = length[b - left] = length[b + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[b]] += 1

            if count[m] > 0:
                res = i + 1

        return res
