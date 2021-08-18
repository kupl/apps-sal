class Solution:
    def maxNonOverlapping(self, A: List[int], target: int) -> int:

        seen = {0}
        prefix_sum = count = 0

        for a in A:
            prefix_sum += a
            if -target + prefix_sum in seen:
                prefix_sum = 0
                count += 1
                seen = set()
            seen.add(prefix_sum)

        return count
