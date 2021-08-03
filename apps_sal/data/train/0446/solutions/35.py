class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        c = collections.Counter(arr)
        for n in sorted(c, key=lambda num: c[num]):
            if c[n] <= k:
                k -= c[n]
                del c[n]
            else:
                break

        return len(c)
