class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
    
        m = max(arr[0], arr[1])
        count = 1
        for i in range(1, len(arr)-1):
            if count >= k:
                return m
            if m > arr[i+1]:
                count += 1
            else:
                m = arr[i+1]
                count = 1
                                  
        return m
