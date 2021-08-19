class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num_odds = defaultdict(int, {0: 1})
        total = 0
        running = 0
        for n in nums:
            running += n % 2
            total += num_odds[running - k]
            num_odds[running] += 1
        return total
