class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] *len(nums)
        start = {}

        prefix_sum[0]= 0 if nums[0]%2==0 else 1
        if prefix_sum[0] == 0:
            start[0] = 0
        else:
            start[1]=0
        
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1] if nums[i]%2==0 else prefix_sum[i-1]+1
            if prefix_sum[i-1]!=prefix_sum[i]:
                start[prefix_sum[i]] = i
        out = 0
        start[prefix_sum[0]] = 0
        start[prefix_sum[len(nums)-1]] = len(nums)-1


        for i in range(len(nums)):
            print(i)
            if prefix_sum[i] >= k and nums[i]%2!=0:
                if prefix_sum[i]-(k-1) in start:
                    beg = start[prefix_sum[i]-(k-1)]
                else:
                    beg = 0
                # count even numbers before beg
                j = beg - 1
                left_count = 0
                while j >=0:
                    if nums[j] %2==0:
                        left_count+=1
                    else:
                        break
                    j-=1
                # count even numbers after i
                j = i+1
                right_count = 0
                while j <len(nums):
                    if nums[j] %2==0:
                        right_count+=1
                    else:
                        break
                    j+=1
                out += ((left_count + 1)*(right_count+1))                        
        return out
