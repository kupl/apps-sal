class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        e2s = {}
        s2e = {}
        cnt = {}
        for (i, v) in enumerate(arr):
            if v - 1 not in e2s and v + 1 not in s2e:
                (l, r) = (v, v)
            elif v - 1 not in e2s and v + 1 in s2e:
                (l, r) = (v, s2e[v + 1])
                del s2e[v + 1]
                cnt[r - v] -= 1
                if not cnt[r - v]:
                    del cnt[r - v]
            elif v - 1 in e2s and v + 1 not in s2e:
                (l, r) = (e2s[v - 1], v)
                del e2s[v - 1]
                cnt[v - l] -= 1
                if not cnt[v - l]:
                    del cnt[v - l]
            else:
                (l, r) = (e2s[v - 1], s2e[v + 1])
                del e2s[v - 1]
                del s2e[v + 1]
                cnt[v - l] -= 1
                if not cnt[v - l]:
                    del cnt[v - l]
                cnt[r - v] -= 1
                if not cnt[r - v]:
                    del cnt[r - v]
            s2e[l] = r
            e2s[r] = l
            cnt[r - l + 1] = cnt.get(r - l + 1, 0) + 1
            if m in cnt:
                res = i + 1
        return res
