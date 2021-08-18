class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
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
        currSum = (float('inf'), -1) 
        while left <= right: 
            mid = left + (right - left) // 2
            checkSum = condition(mid)
            if checkSum < currSum[0]: 
                currSum = (checkSum, mid)
                right = mid - 1
            else:
                left = mid + 1
            print(left, right)
        return currSum[1]
        '''
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

        if abs(target - condition(left)) < abs(target - condition(left - 1)):
            return left
        else:
            return left - 1
