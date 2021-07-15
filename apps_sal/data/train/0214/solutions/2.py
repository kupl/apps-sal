class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        return self.sb(nums)
    
    '''
    걍 even 을 작게만들거나주변보다 혹은 odd를 주변보다 작게만들거나 ㅇㅇ
    '''
    def sb(self, nums):
        nums = [float('inf')] + nums + [float('inf')]
        
        res = [0,0]
        
        for i in range(1, len(nums)-1):
            res[i%2] += max(0, (nums[i] - min(nums[i-1],nums[i+1])+1)) # 주변이 다 나보다 크면 움직이지않아도됌 :) 혹은 나보다 작은애있으면 큰만큼 + 1 줄여야함
        return min(res)
