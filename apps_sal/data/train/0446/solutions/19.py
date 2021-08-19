class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == len(arr):
            return 0
        d = dict()
        for i in arr:
            if i in list(d.keys()):
                d[i] += 1
            else:
                d[i] = 1
        lst = [[v, k] for (k, v) in list(d.items())]
        lst.sort()
        res = []
        for i in lst:
            for _ in range(i[0]):
                res.append(i[1])
        return len(set(res[k:]))
