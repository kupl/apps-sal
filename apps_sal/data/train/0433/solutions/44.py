class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        output = 0
    
        #calculate initial sum
        summ = 0
        for i in range(k):
            summ += arr[i]

        #check initial summ for avg
        if summ / k >= threshold:
            output += 1

        for i in range(k, len(arr)):
            summ = summ + arr[i] - arr[i-k]
            if summ / k >= threshold:
                output += 1

        return output
