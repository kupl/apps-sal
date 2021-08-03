class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        freq = sorted(counter.values())

        ans = len(freq)

        for f in freq:
            if k >= f:
                k -= f
                ans -= 1
        return ans
