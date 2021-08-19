class Solution:

    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        ans = -1
        d = {}
        ls = [0] * (n + 3)
        for (ind, i) in enumerate(a):
            (j, k) = (i - 1, i + 1)
            ls[i] = 1
            (l, r) = (ls[j], ls[k])
            d[l] = d.get(l, 0) - 1
            d[r] = d.get(r, 0) - 1
            d[l + r + 1] = d.get(l + r + 1, 0) + 1
            ls[i - l] = l + r + 1
            ls[i + r] = l + r + 1
            if m in d and d[m] > 0:
                ans = ind + 1
        return ans
