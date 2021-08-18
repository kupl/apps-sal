class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ret = -1
        cnt = [[] for _ in range(len(arr))]
        counter = collections.Counter()
        for (i, n) in enumerate(arr):
            n -= 1
            cnt[n].extend([n, n])
            if n - 1 >= 0 and cnt[n - 1]:
                cnt[n][0] = cnt[n - 1][0]
                counter[cnt[n - 1][1] - cnt[n - 1][0] + 1] -= 1
            if n + 1 < len(arr) and cnt[n + 1]:
                cnt[n][1] = cnt[n + 1][1]
                counter[cnt[n + 1][1] - cnt[n + 1][0] + 1] -= 1

            cnt[cnt[n][0]][1] = cnt[n][1]
            cnt[cnt[n][1]][0] = cnt[n][0]
            counter[cnt[n][1] - cnt[n][0] + 1] += 1

            if counter[m] > 0:
                ret = i + 1

        return ret
