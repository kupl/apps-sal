class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        P = [0]
        for e in nums:
            P.append(P[-1] + e)
        seen = set()
        ans = 0
        for psum in P:
            if psum - target in seen:
                seen = {psum}
                ans += 1
            else:
                seen.add(psum)
        return ans
