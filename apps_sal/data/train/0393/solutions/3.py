class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        
        nums = sorted([a, b, c])
        nums2 = [lcm(a, b), lcm(b, c), lcm(a, c)]
        nums3 = lcm(nums2[0], c)
        
        lo, hi = n, nums[-1] * n
        
        while lo < hi:
            mid = (lo + hi) // 2
            rank = (sum(mid // n for n in nums) - sum(mid//n for n in nums2) + mid // nums3)
            if rank < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
