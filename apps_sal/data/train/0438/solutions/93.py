class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        status = [0] * len(arr)
        cnt = collections.Counter()
        last = -1
        for (step, idx) in enumerate(arr):
            i = idx - 1
            status[i] = 1
            left = not (i == 0 or status[i - 1] == 0)
            right = not (i >= len(arr) - 1 or status[i + 1] == 0)
            if not left and (not right):
                cnt[1] += 1
                status[i] = 1
            elif left and right:
                (j, k) = (status[i - 1], status[i + 1])
                full = 1 + j + k
                status[i - j] = full
                status[i + k] = full
                cnt[full] += 1
                cnt[j] -= 1
                cnt[k] -= 1
            elif left:
                j = status[i - 1]
                full = 1 + j
                status[i - j] = full
                status[i] = full
                cnt[j] -= 1
                cnt[full] += 1
            elif right:
                k = status[i + 1]
                full = 1 + k
                status[i] = full
                status[i + k] = full
                cnt[k] -= 1
                cnt[full] += 1
            if cnt[m] > 0:
                last = step + 1
        return last
