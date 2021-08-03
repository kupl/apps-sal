class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)

        for cnt, num in sorted((v, k) for k, v in c.items()):
            if cnt <= k:
                del c[num]
                k -= cnt

        return len(c)
