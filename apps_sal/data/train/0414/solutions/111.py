class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        cur = arr[0]
        for i in range(1,len(arr)):
            if cur > arr[i]:
                count+=1
            else: 
                count = 1
                cur = arr[i]
            if count == k:
                break
        return cur

