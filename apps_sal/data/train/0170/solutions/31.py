class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        lastPos = len(arr)-1
        stop = False
        idx = len(arr)-2
        while idx > -1 and not stop:
            num = arr[idx]
            prev = arr[lastPos]
            if num <= prev:
                lastPos = idx
            else:
                stop = True
            idx -= 1
        rightSub = lastPos
        
        minSub = rightSub
        idx = 0
        stop = False
        valid = False
        while idx < rightSub and not stop:
            valid = False
            if idx == 0 or arr[idx] >= arr[idx-1]:
                num = arr[idx]
                while rightSub < len(arr) and not valid:
                    numRight = arr[rightSub]
                    if numRight < num:
                        rightSub += 1
                    else:
                        valid = True
                minSub = min(minSub, (rightSub - idx - 1))        
                idx += 1
            else:
                stop = True
            
        idx -= 1
        minSub = min(minSub, (rightSub - idx - 1))
        return minSub
        
        

