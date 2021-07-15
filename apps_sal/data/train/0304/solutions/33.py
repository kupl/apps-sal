class Solution:
    
    def B_search(self, nums, target):
    
        low, high=0, len(nums)-1
        while low<high:
            mid=low+(high -low)//2
            if nums[mid] < target:
                low=mid+1
            else:
                high=mid
        return high
    
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        count = 0
        for age in ages:
            
            left= self.B_search(ages,  int((0.5 * age) + 7)+1)
            right= self.B_search(ages,age+1)
            if right==len(ages)-1 and ages[right]==age:
                right+=1
            
            if ages[left]==(0.5 * age) + 7:
                left+=1
            count += max(0, right - left - 1)                
        return count
