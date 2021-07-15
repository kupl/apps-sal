class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        

        sums = {}
        for i in range(n):
            for j in range(i,n):
                sums[(i,j)] = nums[j]
                if j > i:
                    sums[(i,j)] += sums[(i,j-1)]
                    
        s = sorted(sums.values())
        # print(s)
        # print(s[left-1: right])
        ret = sum(s[left-1: right]) % (10**9 + 7)
        return ret
