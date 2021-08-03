class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counts = Counter(nums)

        for _ in range(len(nums) // k):
            min_val = min(counts.keys())
            for v in range(min_val, min_val + k):
                if v not in counts:
                    return False

                counts[v] -= 1
                if counts[v] == 0:
                    del counts[v]

        return True
