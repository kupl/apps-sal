class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        #brute force, linear scan, TIME LIMIT EXCEEDED
        '''
        sums = []
        for i in range(max(arr)+1):
            currSum = 0 
            for val in arr: 
                if val > i: 
                    currSum += i
                else:
                    currSum += val
            
            sums.append((abs(currSum-target),i))
        sums.sort(key = lambda x:x[0])
        return sums[0][1]
        '''
        
        #linear scan with stopping condition, works! but really bad lol 
        '''
        sums = []
        for i in range(max(arr)+1):
            currSum = 0 
            for val in arr: 
                if val > i: 
                    currSum += i
                else:
                    currSum += val
            if currSum-target > 0:
                sums.append((abs(currSum-target),i))
                break
            else:
                sums.append((abs(currSum-target),i))
        sums.sort(key = lambda x:x[0])
        return sums[0][1]
        '''
        
        #binary search, find the minimum integer that meets stopping condition
        #since you are trying to minimize the difference, stop on the smallest one and find the corresponding value 
        '''
        def condition(cutoff): 
            currSum = 0
            for val in arr: 
                if val > cutoff: 
                    currSum += cutoff
                else:
                    currSum += val
            return abs(currSum - target)
            
        left, right = 0, target
        currSum = (float('inf'), -1) #smallest sum, the cutoff value which gives you the smallest sum 
        while left <= right: 
            mid = left + (right - left) // 2
            checkSum = condition(mid)
            if checkSum < currSum[0]: #if the smallest sum is smaller than the previous smallest sum, store the cutoff value
                currSum = (checkSum, mid)
                right = mid - 1
            else:
                left = mid + 1
            print(left, right)
        return currSum[1]
        '''
        #binary search but look for the cutoff point
        def condition(cutoff): 
            currSum = 0
            for val in arr: 
                if val > cutoff: 
                    currSum += cutoff
                else:
                    currSum += val
            return currSum   
        
        left, right = 0, max(arr)
        while left < right: 
            mid = left + (right - left) // 2
            if condition(mid) < target:
                left = mid + 1
            else:
                right = mid 

        if abs(target-condition(left)) < abs(target-condition(left-1)): 
            return left
        else:
            return left - 1
        
        
        

