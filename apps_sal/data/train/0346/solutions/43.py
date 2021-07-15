class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        last = 0
        hsh = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
                
            nums[i] += last
            last = nums[i]
            if nums[i] not in hsh:
                hsh[nums[i]] = []
            hsh[nums[i]].append(i)
        
        count = 0
        if k in hsh:
            count = len(hsh[k])
        
        for i in range(len(nums)):
            x = nums[i]
            if x + k in hsh:
                for v in hsh[x+k][::-1]:
                    if v < i:
                        break
                    count += 1
        return count
                
            
            
        
                
        

