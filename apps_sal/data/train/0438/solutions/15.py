class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        # my solution ... 1332 ms ... 80 % ... 27.5 MB ... 98 %
        #  time: O(n)
        # space: O(n)

        if m == len(arr):
            return m
        res = -1
        e2s = {}  # e2s[5] = 3 表示 3-4-5 位置现在均为1。此时必有s2e[3] = 5
        s2e = {}
        cnt = {}  # cnt[3] = 8 表示此时有 8 个 '111'
        for i, v in enumerate(arr):  # i+1 是当前 step，v是当前step从0变为1的位置，其两侧的索引为v-1和v+1
            if v - 1 not in e2s and v + 1 not in s2e:
                l, r = v, v
            elif v - 1 not in e2s and v + 1 in s2e:
                l, r = v, s2e[v + 1]
                del s2e[v + 1]
                cnt[r - v] -= 1
                if not cnt[r - v]:
                    del cnt[r - v]
            elif v - 1 in e2s and v + 1 not in s2e:
                l, r = e2s[v - 1], v
                del e2s[v - 1]
                cnt[v - l] -= 1
                if not cnt[v - l]:
                    del cnt[v - l]
            else:
                l, r = e2s[v - 1], s2e[v + 1]  # 位置 v 变为 1 后，v 左侧最远 1 及 v 右侧最远 1
                del e2s[v - 1]
                del s2e[v + 1]
                cnt[v - l] -= 1  # 更新旧的频次
                if not cnt[v - l]:
                    del cnt[v - l]
                cnt[r - v] -= 1
                if not cnt[r - v]:
                    del cnt[r - v]
            s2e[l] = r
            e2s[r] = l
            cnt[r - l + 1] = cnt.get(r - l + 1, 0) + 1  # 增加新的频次
            if m in cnt:
                res = i + 1
        return res
