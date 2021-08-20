class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        ls = []
        for (i, c) in c.items():
            ls.append((c, i))
        ls.sort(reverse=True)
        l = 0
        r = len(ls) - 1
        res = 0
        items = 0
        for i in range(len(ls)):
            res += 1
            items += ls[i][0]
            if items >= len(arr) // 2:
                break
        return res
