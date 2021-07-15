
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        numPos, numNeg = 0,0
        
        for num in arr:
            if num >= 0:
                numPos += 1
            else:
                numNeg += 1
        
        if numPos == len(arr):
            return sum(arr)*k
        
        if numNeg == len(arr):
            return 0
        
        # Check for 2* arr
        arrTwo = arr*2
        for i in range(1, len(arrTwo)):
            if arrTwo[i - 1] > 0: 
                arrTwo[i] +=arrTwo[i - 1]
                
        # Check for 3*arr
        arrThree = arr*3
        for i in range(1, len(arrThree)):
            if arrThree[i - 1] > 0: 
                arrThree[i] +=arrThree[i - 1]
        
        arrDiff = max(arrThree) - max(arrTwo)
        
        
        return (max(arrTwo) + (k-2)*arrDiff) % (10**9 + 7)
        
            
        
       
        

