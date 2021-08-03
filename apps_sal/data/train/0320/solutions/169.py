class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 1:
            v = nums[0]
            while v:
                if v % 2:
                    ans += 1
                    v -= 1
                if v:
                    v //= 2
                    ans += 1
            return ans
        c = collections.Counter()
        for i, v in enumerate(nums):
            if v % 2:
                nums[i] -= 1
                ans += 1
            c[nums[i]] += 1
        two = 0
        for v in sorted(c.keys()):
            temp = 0
            t = 0
            u = v
            while v:
                if v % 2:
                    t += 1
                    v -= 1
                if v:
                    v //= 2
                    temp += 1
            ans += t * c[u] + (temp - two)
            two += (temp - two)

        return ans
