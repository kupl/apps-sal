class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        mp = Counter()
        n = len(arr)
        v = [False] * (n + 1)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for (i, a) in enumerate(arr):
            v[a] = True
            mp[1] += 1
            left[a] = a
            right[a] = a
            if a - 1 > 0 and v[a - 1]:
                mp[right[a] - left[a] + 1] -= 1
                mp[right[a - 1] - left[a - 1] + 1] -= 1
                ll = left[a - 1]
                rr = right[a]
                left[ll] = left[rr] = ll
                right[rr] = right[ll] = rr
                mp[rr - ll + 1] += 1
            if a + 1 <= n and v[a + 1]:
                mp[right[a] - left[a] + 1] -= 1
                mp[right[a + 1] - left[a + 1] + 1] -= 1
                ll = left[a]
                rr = right[a + 1]
                left[ll] = left[rr] = ll
                right[rr] = right[ll] = rr
                mp[rr - ll + 1] += 1
            if mp[m] != 0:
                res = i + 1
        return res
