class Solution:

    def isEscapePossible(self, blocked: List[List[int]], se: List[int], target: List[int]) -> bool:
        d = {}
        d[se[0], se[1]] = 1
        e = [se]
        v = 1
        bl = {tuple(i) for i in blocked}
        g = 0
        while e != []:
            f = []
            for i in e:
                if i == target:
                    return True
                x = i[0]
                y = i[1]
                if abs(x - se[0]) + abs(y - se[1]) > 200:
                    g = 2
                    break
                if x > 0:
                    if (x - 1, y) not in bl and (x - 1, y) not in d:
                        f.append([x - 1, y])
                        d[x - 1, y] = 1
                if x < 10 ** 6:
                    if (x + 1, y) not in bl and (x + 1, y) not in d:
                        f.append([x + 1, y])
                        d[x + 1, y] = 1
                if y > 0:
                    if (x, y - 1) not in bl and (x, y - 1) not in d:
                        f.append([x, y - 1])
                        d[x, y - 1] = 1
                if y < 10 ** 6:
                    if (x, y + 1) not in bl and (x, y + 1) not in d:
                        f.append([x, y + 1])
                        d[x, y + 1] = 1
            if g == 2:
                break
            e = f
        if e == []:
            return False
        d = {}
        d[target[0], target[1]] = 1
        e = [target]
        v = 0
        while e != []:
            f = []
            for i in e:
                if i == se:
                    return True
                x = i[0]
                y = i[1]
                if abs(x - se[0]) + abs(y - se[1]) > 200:
                    return True
                if x > 0:
                    if (x - 1, y) not in bl and (x - 1, y) not in d:
                        f.append([x - 1, y])
                        d[x - 1, y] = 1
                if x < 10 ** 6:
                    if (x + 1, y) not in bl and (x + 1, y) not in d:
                        f.append([x + 1, y])
                        d[x + 1, y] = 1
                if y > 0:
                    if (x, y - 1) not in bl and (x, y - 1) not in d:
                        f.append([x, y - 1])
                        d[x, y - 1] = 1
                if y < 10 ** 6:
                    if (x, y + 1) not in bl and (x, y + 1) not in d:
                        f.append([x, y + 1])
                        d[x, y + 1] = 1
            e = f
        if e == []:
            return False
