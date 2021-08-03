import collections


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [0] + arr + [0]
        N = len(arr)
        left = [0] * N
        right = [0] * N
        sizes = collections.Counter()
        ans = 0
        for i in range(1, N - 1):
            l = left[arr[i] - 1]
            r = right[arr[i] + 1]

            sizes[l] -= 1

            sizes[r] -= 1
            sizes[l + r + 1] += 1
            left[arr[i] + 1 + r - 1] = l + r + 1
            right[arr[i] - 1 - l + 1] = l + r + 1
            if sizes[m] >= 1:
                ans = i

        return ans if ans >= 1 else -1
