class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxi = max(arr)
        cur = count = 0
        for i, value in enumerate(arr):
            if value == maxi:
                return maxi
            
            if value > cur:
                if i == 0:
                    cur, count = value, 0
                else:
                    cur, count = value, 1
            else:
                count += 1
                
            if count == k:
                return cur
