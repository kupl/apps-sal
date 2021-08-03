class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        di = collections.defaultdict(int)
        for v in arr:
            di[v] += 1
        ar = sorted([v for k, v in list(di.items())], reverse=True)
        while ar and k >= ar[-1]:
            k -= ar.pop()
        return len(ar)
