class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        acnt = collections.Counter(arr)
        nt = [[val, key] for key, val in acnt.items()]
        heapq.heapify(nt)
        while k > 0:
            fre, val = heapq.heappop(nt)
            k -= fre
        if k == 0:
            return len(nt)
        return len(nt) + 1
