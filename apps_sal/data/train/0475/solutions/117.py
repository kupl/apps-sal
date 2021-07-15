class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        i,j,s = 0,0,0
        total = []
        while i < n:
            if j == n-1:
                s += nums[j]
                total.append(s)
                i += 1
                j= i
                s = 0
            else:
                if i == j:
                    s = nums[j]
                    total.append(s)
                    j += 1
                else:
                    s += nums[j]
                    total.append(s)
                    j += 1
        total.sort()
        return (sum(total[left-1:right]) %(10**9+7))
