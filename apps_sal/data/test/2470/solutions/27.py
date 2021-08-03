class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:

        dp = {-1: 0}
        B = sorted(B)

        for cur in A:
            temp = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if prev < cur:
                    temp[cur] = min(temp[cur], dp[prev])
                idx = self.upper_bound(B, prev)
                if idx < len(B):
                    temp[B[idx]] = min(temp[B[idx]], dp[prev] + 1)
            dp = temp

        if dp:
            return min(dp.values())
        return -1

    def upper_bound(self, B, target):
        l = 0
        r = len(B)
        while l < r:
            mid = l + (r - l) // 2
            if B[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
