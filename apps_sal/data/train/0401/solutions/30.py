class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total%3 == 0:
            return total
        nums_set = set(nums)
        div, mod = divmod(total, 3)
        nums.sort()
        while mod <= total:
            if mod in nums_set:
                return div*3
            for i in range(n-2):
                sum_val = 0
                if nums[i] > mod:
                    break
                for j in range(i+1, n-1):
                    if nums[i] + nums[j] == mod:
                        return div*3    
                    for k in range(j+1, n):
                        #print(i, j, k)
                        #print(nums[i], nums[j:k])
                        sum_val += nums[i] + sum(nums[j:k])
                        if sum_val == mod:
                            return div*3
                        if sum_val > mod:
                            break     

            div -= 1
            mod += 3
