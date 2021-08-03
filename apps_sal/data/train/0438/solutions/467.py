class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        p = [i for i in range(n)]
        l = [0 for i in range(n)]
        s = [0 for i in range(n)]
        counts = collections.Counter()
        res = []

        def find(a):
            if p[a] == a:
                return a
            p[a] = find(p[a])

            return p[a]

        def union(a, b):
            p_a, p_b = find(a), find(b)
            if p[p_b] != p[p_a]:
                p[p_b] = p[p_a]
                l[p_a] += l[p_b]
        for v in arr:
            i = v - 1
            s[i] = 1
            l[i] = 1
            f_a = f_b = False
            if i + 1 < n and s[i + 1] == 1:
                counts[l[find(i + 1)]] -= 1
                union(i, i + 1)
                f_a = True
            if i - 1 >= 0 and s[i - 1] == 1:
                counts[l[find(i - 1)]] -= 1
                union(i - 1, i)
                f_b = True
            if f_a and f_b:
                counts[l[find(i - 1)]] += 1
            elif f_a:
                counts[l[find(i)]] += 1
            elif f_b:
                counts[l[find(i - 1)]] += 1
            else:
                counts[l[find(i)]] += 1
            res.append(counts[m])

        for i in range(n - 1, -1, -1):
            if res[i] > 0:
                return i + 1

        return -1
