class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        move = -1
        l = {x: (0, 0) for x in range(len(arr) + 2)}
        for (i, a) in enumerate(arr):
            l[a] = (a, a)
            (b, c) = (a, a)
            if l[a - 1][0]:
                if l[a - 1][1] - l[a - 1][0] + 1 == m:
                    move = i
                b = l[a - 1][0]
            if l[a + 1][0]:
                if l[a + 1][1] - l[a + 1][0] + 1 == m:
                    move = i
                c = l[a + 1][1]
            l[a] = (b, c)
            l[b] = (b, c)
            l[c] = (b, c)
            if l[a][1] - l[a][0] + 1 == m:
                move = i + 1
        return move
