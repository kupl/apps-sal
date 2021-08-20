class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        h = {}
        for i in arr:
            if not i in h:
                h[i] = 0
            h[i] += 1
        v = sorted(list(h.values()), reverse=True)
        m = len(arr)
        t = 0
        p = 0
        i = 0
        print(v)
        while t < m // 2:
            t += v[i]
            i += 1
            p += 1
        return p
