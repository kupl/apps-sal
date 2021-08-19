class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def dfs(m):
            r = 0
            for i in nums:
                r += math.ceil(i / m)
                if r > threshold:
                    return False
            return True
        (l, r) = (1, int(1000000.0))
        while l <= r:
            m = (l + r) // 2
            if dfs(m):
                r = m - 1
            else:
                l = m + 1
        return l
        '\n        for i in range(1,max(nums)):\n            r=0\n            n-=1\n            for j in nums:\n                if j%i==0:\n                    r+=j//i\n                else:\n                    r+=(j//i)+1\n            if r<=threshold:\n                return i\n        '
