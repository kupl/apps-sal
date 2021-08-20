class Solution:

    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        sz = {}
        cnt = Counter()
        ret = -1
        for (i, x) in zip(list(range(1, n + 1)), a):
            left = sz[x - 1] if x - 1 in sz else 0
            right = sz[x + 1] if x + 1 in sz else 0
            tot = left + right + 1
            sz[x - left] = tot
            sz[x + right] = tot
            cnt[left] -= 1
            cnt[right] -= 1
            cnt[tot] += 1
            if cnt[m]:
                ret = i
        return ret
