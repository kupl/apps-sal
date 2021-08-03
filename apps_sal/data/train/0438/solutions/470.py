class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # union find

        dsu = [False] * (len(arr) + 1)
        dsu[0] = 0

        def find(a):
            if dsu[a] == False:
                dsu[a] = -1
                return a
            x = []
            while dsu[a] >= 0:
                x.append(a)
                a = dsu[a]
            for b in x:
                dsu[b] = a
            return a

        def size(a):
            pa = find(a)
            return abs(dsu[pa])

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if dsu[pa] < dsu[pb]:
                    dsu[pa] += dsu[pb]
                    dsu[pb] = pa
                else:
                    dsu[pb] += dsu[pa]
                    dsu[pa] = pb
                return True
            return False
        ans = -1
        for i, x in enumerate(arr, 1):
            find(x)
            if x > 1 and dsu[x - 1] != False:
                if size(x - 1) == m:
                    dsu[0] -= 1
                union(x, x - 1)
            if x < len(arr) and dsu[x + 1] != False:
                if size(x + 1) == m:
                    dsu[0] -= 1
                union(x, x + 1)
            if size(x) == m:
                dsu[0] += 1
            # print(dsu[0])
            if dsu[0] > 0:
                ans = i
        return ans
