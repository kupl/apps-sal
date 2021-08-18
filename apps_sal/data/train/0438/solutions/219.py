class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        d = {}
        res = set()
        ans = -1
        for (s, j) in enumerate(arr):
            i = j - 1
            if i + 1 not in d and i - 1 not in d:
                d[i] = 1
                if d[i] == m:
                    res.add(i)
            elif i + 1 in d and i - 1 not in d:
                if i + 1 in res:
                    res.remove(i + 1)
                if i + d[i + 1] in res:
                    res.remove(i + d[i + 1])
                if d[i + 1] != 1:
                    temp = d.pop(i + 1)
                    d[i] = 1 + temp
                    d[i + temp] += 1
                else:
                    d[i] = 2
                    d[i + 1] = 2
                if d[i] == m:
                    res.add(i)

            elif i - 1 in d and i + 1 not in d:
                if i - 1 in res:
                    res.remove(i - 1)
                if i - d[i - 1] in res:
                    res.remove(i - d[i - 1])
                if d[i - 1] != 1:
                    temp = d.pop(i - 1)
                    d[i] = 1 + temp
                    d[i - temp] += 1
                else:
                    d[i] = 2
                    d[i - 1] = 2
                if d[i] == m:
                    res.add(i)

            else:
                a, b = i - d[i - 1], i + d[i + 1]
                if d[i - 1] != 1:
                    d.pop(i - 1)
                if d[i + 1] != 1:
                    d.pop(i + 1)
                if i - 1 in res:
                    res.remove(i - 1)
                if i + 1 in res:
                    res.remove(i + 1)
                if a in res:
                    res.remove(a)
                if b in res:
                    res.remove(b)
                d[a] = b - a + 1
                d[b] = b - a + 1
                if b - a + 1 == m:
                    res.add(a)
                    res.add(b)

            if res:
                ans = s + 1
        return ans
