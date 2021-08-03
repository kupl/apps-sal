class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        from collections import Counter
        from heapq import heappush, heappop
        d = Counter(arr)
        q = []

        for ele in d:

            heappush(q, [d[ele], ele])
        print(q)
        for i in range(k):
            temp = q[0]
            if temp[0] == 1:
                print(temp)
                heappop(q)
            else:
                temp[0] -= 1
        return len(q)
