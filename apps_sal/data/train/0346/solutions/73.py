class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        ans = 0
        p1 = p2 = p3 = p4 = -1
        while p4 < n:
            p2 += 1
            while p2 < n and nums[p2] % 2 == 0:
                p2 += 1
                if p2 == n:
                    return ans
            if p4 == -1:
                p3 = p2
                remaining = k - 1
                while p3 < n and remaining:
                    p3 += 1
                    if p3 == n:
                        return ans
                    if nums[p3] % 2 == 1:
                        remaining -= 1
            else:
                p3 = p4
            p4 = p3 + 1
            while p4 < n:
                if nums[p4] % 2 == 1:
                    break
                p4 += 1
            ans += (p2 - p1) * (p4 - p3)
            p1 = p2
        return ans
