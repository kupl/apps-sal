class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        end = k

        count = 0

        #Sum the values initially as a buffer
        sumInit = sum(arr[start:end])                                   

        #To check if the average exceeds threshold if yes increase count by 1
        if ((sumInit / k) >= threshold):                                
            count += 1

        #To check end is within limits
        while end < len(arr):   
            #Subtract the start and end
            sumInit = sumInit - arr[start] + arr[end]
            #Check if average exceeds threshold
            if ((sumInit / k) >= threshold):
                count += 1
            start += 1
            end += 1



        return count
