class Solution:
    def minRefuelStops(self, t: int, f: int, st: List[List[int]]) -> int:
        if f >= t:
            return 0
        if st == []:
            return -1
        if f < st[0][0]:
            return -1
        li, li1 = [], []
        for i, j in st:
            li.append(i)
            li1.append(j)
        count = 0
        while f < t:
            s, tur = 0, []
            for i in li:
                if f >= i:
                    s = li.index(i)
                    tur.append(True)
                else:
                    tur.append(False)
            print(tur)
            if all(i == False for i in tur):
                return -1
            f += max(li1[0:s + 1])
            li.pop(li1.index(max(li1[0:s + 1])))
            li1.remove(max(li1[0:s + 1]))
            count += 1
        return count
