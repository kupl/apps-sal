class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        A.sort()

        if 0 in d:
            if d[0] % 2 != 0:
                return False
            d.pop(0)

        for i in A:
            if i not in d:
                continue

            if i * 2 in d:
                if d[i] > d[i * 2]:
                    d[i] -= d[i * 2]
                    d[i * 2] = 0
                else:
                    d[i * 2] -= d[i]
                    d[i] = 0
                if d[i] == 0:
                    d.pop(i)
                if d[i * 2] == 0:
                    d.pop(i * 2)
            elif i % 2 == 0 and i // 2 in d:
                if d[i] > d[i // 2]:
                    d[i] -= d[i // 2]
                    d[i // 2] = 0
                else:
                    d[i // 2] -= d[i]
                    d[i] = 0
                if d[i] == 0:
                    d.pop(i)
                if d[i // 2] == 0:
                    d.pop(i // 2)
            else:
                return False
        return len(d) == 0
