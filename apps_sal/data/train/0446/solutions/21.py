class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        import collections
        d = collections.Counter(arr).most_common()[::-1]
        for i in range(len(d)):
            k -= d[i][1]
            if k < 0:
                return len(d) - i
        return 0
