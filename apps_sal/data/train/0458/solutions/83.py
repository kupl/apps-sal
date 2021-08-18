from collections import defaultdict


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        psums = [0]
        for n in nums:
            psums.append((psums[-1] + n) % p)

        ssums = [0]
        for n in reversed(nums):
            ssums.append((ssums[-1] + n) % p)

        ssumd = defaultdict(list)
        for i, s in enumerate(reversed(ssums)):
            ssumd[s].append(i)

        best = len(nums)
        matched = set()
        for ri, n in enumerate(reversed(psums)):
            i = len(psums) - ri - 1
            match = -n % p
            if match in matched:
                continue
            for j in ssumd[match]:
                if j >= i:
                    best = min(best, j - i)
                    matched.add(match)

        if best == len(nums):
            return -1

        return best
