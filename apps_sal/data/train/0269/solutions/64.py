class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        h = defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)
        if not h[1]:
            return True
        return all([h[1][i] - h[1][i - 1] > k for i in range(1, len(h[1]))])
