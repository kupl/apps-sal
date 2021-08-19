class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dic = collections.Counter()
        cnt = collections.Counter()
        res = -1
        for (i, a) in enumerate(arr):
            l = dic[a - 1]
            r = dic[a + 1]
            dic[a - l] = dic[a + r] = dic[a] = l + r + 1
            cnt[l + r + 1] += 1
            cnt[l] -= 1
            cnt[r] -= 1
            if cnt[m]:
                res = i + 1
        return res
