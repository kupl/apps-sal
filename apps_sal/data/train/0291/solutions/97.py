class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # count of odd numbers, counts of even sums and odd sums
        # default 1 for counts of even sums means 0 even sum is also a valid combination
        odds, counts = 0, [1, 0]
        for x in arr:
            odds += 1 if x % 2 else 0
            counts[odds % 2] += 1
        return counts[0] * counts[1] % (10**9 + 7)
