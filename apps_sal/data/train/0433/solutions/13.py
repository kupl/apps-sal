class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        size = len(arr)
        
        avg = sum(arr[:k]) / k
        count = 1 if avg >= threshold else 0
        
        end = k
        
        while end < size:
            prevVal = arr[end-k] / k
            nextVal = arr[end] / k
            
            avg += nextVal - prevVal
            
            count += 1 if avg >= threshold else 0
            end += 1
            
        return count
        

