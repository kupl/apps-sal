class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ids = [0] * (len(arr) + 2)
        d = []
        lst = -1

        def parent(a):
            # print(a)
            if(ids[a] < 0):
                return a
            ids[a] = parent(ids[a])
            return ids[a]

        def SF(a, b):
            return parent(a) == parent(b)

        def SU(a, b):
            a = parent(a)
            b = parent(b)
            # print(a,\" \",b)
            if(a == b):
                return
            if(ids[a] <= ids[b]):
                ids[a] += ids[b]
                ids[b] = a
            else:
                ids[b] += ids[a]
                ids[a] = b

        def size(a):
            return -ids[parent(a)]

        for j, i in enumerate(arr):
            # print(\"toto \",j, \"  \",i)
            ids[i] = -1
            if(ids[i - 1] != 0):
                SU(i - 1, i)
            if(ids[i + 1] != 0):
                SU(i, i + 1)
            # print(i,\" \",size(i))
            if(size(i) == m):
                d.append(i)
            for t in range(len(d) - 1, -1, -1):
                x = d.pop(t)
                if(size(x) == m):
                    d.append(x)
                    lst = j + 1
            # print(d)

        return lst
