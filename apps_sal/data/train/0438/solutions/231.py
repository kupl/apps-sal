class Solution:

    def findLatestStep(self, a: List[int], m: int) -> int:
        g = [0] * (len(a) + 1)
        cnt = Counter()
        last = -1
        for (i, p) in enumerate(a):
            l = g[p - 1] if p > 1 else 0
            r = g[p + 1] if p < len(g) - 1 else 0
            new_l = l + 1 + r
            g[p - l] = g[p + r] = new_l
            if l > 0:
                cnt[l] -= 1
                if cnt[l] == 0:
                    del cnt[l]
            if r > 0:
                cnt[r] -= 1
                if cnt[r] == 0:
                    del cnt[r]
            cnt[new_l] += 1
            if m in cnt:
                last = i + 1
        return last
