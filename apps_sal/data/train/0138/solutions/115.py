class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # print(nums)
        if not nums:
            return 0
        memo = collections.defaultdict(list)
        for i,v in enumerate(nums):
            memo[v].append(i)
            
        if 0 in memo:
            arr1 = []
            for j in range(len(memo[0])):
                if j==0:
                    arr1.append(self.getMaxLen(nums[:memo[0][j]]))
                else:
                    arr1.append(self.getMaxLen(nums[memo[0][j-1]+1:memo[0][j]]))
                           
            arr1.append(self.getMaxLen(nums[memo[0][-1]+1:]))
            return max(arr1)
            # return max(self.getMaxLen(nums[:memo[0]]), self.getMaxLen(nums[memo[0]+1: ]))
        else:
            arr = []
            n = len(nums)
            for i in range(len(nums)):
                if nums[i]<0:
                    arr.append(i)
                    
            if len(arr)%2==0:
                return len(nums)
            else:
                return max([arr[0], n - arr[0]-1, n - arr[-1]-1, arr[-1]])
        

