from sortedcontainers import SortedSet
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        # 11111 -> 11101
        # [(start, end)]  , (1,5) => (1,3), 4, (5,5)
        ans = n
        if m == n:
            return ans
        ss = SortedSet([(1, n)])
        s0 = set()
        # print(ss)
        # 1110 1111
        
        for i in range(n-1, -1, -1):
            v = arr[i]
            i_itv = ss.bisect_right((v,n)) - 1
            # print(\"idx:\", i_itv)
            start, end = ss[i_itv]
            # print(start, end, \"v:\",v)
            if (v-start == m) or (end-v == m):
                return i
            ss.discard((start,end))
            if v-1 >= start:
                ss.add((start,v-1))
            if end >= v+1:
                ss.add((v+1,end))
            # print(ss)
        
        return -1
