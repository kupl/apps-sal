class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        blocks = [0]
        for num in nums:
            if num % 2 == 1:
                blocks.append(0)
                continue
            blocks[-1] += 1
        ans = 0
        for (left, right) in zip(blocks, blocks[k:]):
            ans += (left + 1) * (right + 1)
        return ans
