class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tmp = [sum(arr[:k])]
        
        for i in range(k, len(arr)):
            temp = tmp[-1]
            temp = temp - arr[i - k] + arr[i]
            tmp.append(temp)
            
        print(tmp)
        
        count = 0
        
        for el in tmp:
            if el / k >= threshold:
                count += 1
        
        return count
