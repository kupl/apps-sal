class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        N = len(arr)
        rank = [0] * N
        res = -1
        for (i, n) in enumerate(arr):
            n -= 1
            if n != 0 and n != N - 1 and rank[n - 1] and rank[n + 1]:
                cnt[rank[n - 1]] -= 1
                cnt[rank[n + 1]] -= 1
                r = 1 + rank[n - 1] + rank[n + 1]
                cnt[r] += 1
                rank[n + 1 + rank[n + 1] - 1] = r
                rank[n - 1 - rank[n - 1] + 1] = r
            elif n != 0 and rank[n - 1]:
                cnt[rank[n - 1]] -= 1
                cnt[rank[n - 1] + 1] += 1
                rank[n] = rank[n - 1] + 1
                rank[n - 1 - rank[n - 1] + 1] = rank[n]
            elif n != N - 1 and rank[n + 1]:
                cnt[rank[n + 1]] -= 1
                cnt[rank[n + 1] + 1] += 1
                rank[n] = rank[n + 1] + 1
                rank[n + 1 + rank[n + 1] - 1] = rank[n]
            else:
                cnt[1] += 1
                rank[n] = 1
            if cnt[m]:
                res = i + 1
        return res
