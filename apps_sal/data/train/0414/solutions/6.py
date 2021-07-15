class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        rounds = 0         
        count = 0 
        
        while True:
            #print(arr)
            rounds += 1
            if k == 1 and arr[0]<arr[1] or max(arr[1:k+1-count]) > arr[0]:
                i = 1 
                while arr[0] > arr[i]:
                    i += 1
                temp = arr[0]
                loser = arr[1:i]
                winner = arr[i:]
                arr = winner + loser + [temp]
                count = 1 
                if k == 1:
                    return arr[0]
            else:
                return arr[0]
            
        return arr[0]
