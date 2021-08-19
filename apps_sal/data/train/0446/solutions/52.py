class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a = collections.Counter(arr)
        b = sorted(a, key=lambda x: a[x])
        i = 0
        while k:
            if a[b[i]] <= k:
                k -= a[b[i]]
                del b[i]
            else:
                k = 0
        return len(b)
