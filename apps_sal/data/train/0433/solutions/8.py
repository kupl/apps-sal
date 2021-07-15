class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        count = 0
        threshold = threshold * k
        avg = sum(arr[start:k])
        i = k
        while i <= len(arr):
            if start != 0:
                avg = avg - arr[start-1] + arr[i-1]
            if avg >= threshold:
                count += 1
                start += 1
                i = start + k
            else:
                start += 1
                i += 1
        
        return count
        
        
        

