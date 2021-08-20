class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        d = {}
        first = -1
        second = -1
        i = 0
        n = len(tree)
        m = -1
        while i < n:
            if tree[i] in d:
                d[tree[i]].append(i)
                i += 1
            elif len(list(d.keys())) == 2:
                s = 0
                for (k, v) in list(d.items()):
                    s += len(v)
                m = max(m, s)
                if d[first][-1] > d[second][-1]:
                    i = d[second][-1] + 1
                    first = first
                    d = {}
                    d[tree[i]] = [i]
                    i += 1
                else:
                    i = d[first][-1] + 1
                    first = second
                    d = {}
                    d[tree[i]] = [i]
                    i += 1
            elif len(list(d.keys())) == 1:
                second = tree[i]
                d[tree[i]] = [i]
                i += 1
            else:
                first = tree[i]
                d[tree[i]] = [i]
                i += 1
        s = 0
        for (k, v) in list(d.items()):
            s += len(v)
        return max(m, s)
