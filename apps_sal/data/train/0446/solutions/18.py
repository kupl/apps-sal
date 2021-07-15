class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        temp = sorted(c, key= lambda x: (c[x], -x))
        for i in temp:
            if k > 0:
                k -= c[i]
                if k < 0:
                    c[i] = -k
                else:
                    c[i] = 0
        return sum(c[i] > 0 for i in c)
                

