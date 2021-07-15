class Solution:
    def numOfSubarrays(self, coll: List[int]) -> int:
        n = len(coll)
        m = 10**9 + 7
        acc = 0
        evens = odds = 0

        for i, x in enumerate(coll):
            if x & 1:
                evens, odds = odds, evens + 1
            else:
                evens += 1
            
            acc += odds
            acc %= m

        return acc
