class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        s1 = set()
        s2 = set()

        for j, row in enumerate(img1):
            for i, v in enumerate(row):
                if v == 1:
                    s1.add((j, i))
        for j, row in enumerate(img2):
            for i, v in enumerate(row):
                if v == 1:
                    s2.add((j, i))

        d = {}

        for x in s1:
            for y in s2:
                v0 = x[0] - y[0]
                v1 = x[1] - y[1]

                vv = (v0, v1)
                if vv in d:
                    d[vv] += 1
                else:
                    d[vv] = 1

        dl = sorted(list(d.items()), key=lambda x: x[1])

        if not len(dl):
            return 0

        return dl[-1][1]
