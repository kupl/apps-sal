class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ## there's definitely a dfs approach, but it seems
        # expensive...need as many recursive calls per level
        # as the length of the list +1 for op 1
        # start is [0,0]
        # can we extract the solution from the binary rep of all the nums?
        #pad to 32 bit or 
        N = len(nums);
        ansr = 0;
        while(any(nums)):
            divideByTwo = False;
            for i in range(N):
                if(nums[i] == 1):
                    ansr+=1;
                    nums[i] = 0;
                elif(nums[i]==0):
                    continue;
                else:
                    divideByTwo = True
                    if(nums[i]%2 == 1):
                        ansr+=1
                    nums[i] = nums[i]//2
            if(divideByTwo):
                ansr+=1;
        return ansr;
                    

