class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cache = {0: [-1]}
        cnt = 0
        odds = 0
        for i, num in enumerate(nums):
            if num % 2:
                odds += 1
            if odds - k in cache:
                cnt += len(cache[odds-k])
            x = cache.setdefault(odds, [])
            x.append(odds)
        return cnt
