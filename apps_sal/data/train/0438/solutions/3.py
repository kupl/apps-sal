class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        count = [0] * (n + 2)
        lens = [0] * (n + 2)
        res = -1
        for (i, a) in enumerate(arr):
            if lens[a]:
                continue
            l = lens[a - 1]
            r = lens[a + 1]
            t = l + r + 1
            lens[a] = lens[a - l] = lens[a + r] = t
            count[l] -= 1
            count[r] -= 1
            count[t] += 1
            if count[m]:
                res = i + 1
        return res
