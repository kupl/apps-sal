from collections import defaultdict


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        b = [0] * (n + 2)
        cnt = defaultdict(lambda: 0)
        latest = -1
        for i in range(n):
            left = b[arr[i] - 1]
            right = b[arr[i] + 1]
            if left > 0 and right == 0:
                b[arr[i]] += 1 + left
                b[arr[i] - 1 - left + 1] += 1
                cnt[left] -= 1
                cnt[left + 1] += 1
            elif left == 0 and right > 0:
                b[arr[i]] += 1 + right
                b[arr[i] + 1 + right - 1] += 1
                cnt[right] -= 1
                cnt[right + 1] += 1
            elif left > 0 and right > 0:
                b[arr[i] - 1 - left + 1] += 1 + right
                b[arr[i] + 1 + right - 1] += 1 + left
                cnt[right] -= 1
                cnt[left] -= 1
                cnt[1 + left + right] += 1
            else:
                b[arr[i]] += 1
                cnt[1] += 1
            if m in cnt:
                if cnt[m] > 0:
                    latest = i + 1
        return latest
