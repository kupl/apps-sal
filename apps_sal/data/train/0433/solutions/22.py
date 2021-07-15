class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        answer = 0
        
        initial_sum = sum(arr[:k])
        
        for i in range(len(arr) - k + 1):
            if i == 0:
                if initial_sum / k >= threshold:
                    answer += 1
            else:
                initial_sum = initial_sum - arr[i - 1] + arr[i + k - 1]
                if initial_sum / k >= threshold:
                    answer += 1
                
        return answer
