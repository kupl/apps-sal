class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_div = 0
        max_sub = 0
        for num in nums:
            div_times, sub_times = self.calc_steps(num)
            max_div = max(max_div, div_times)
            max_sub +=  sub_times
        return max_div + max_sub
        
    #返回除2的次数和减1的次数
    @lru_cache
    def calc_steps(self, num):
        if num == 0:
            return 0,0
        if num == 1:
            return 0,1
        if num == 2:
            return 1,1
        if num == 3:
            return 1,2
        
        div_times, sub_times = self.calc_steps(num//2)
        
        return div_times+1, num % 2 + sub_times
