class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        blocks = [1]
        for num in nums:
            if num % 2 == 1:
                blocks.append(1)
                continue
            blocks[-1] += 1
        return sum((left * right for (left, right) in zip(blocks, blocks[k:])))
