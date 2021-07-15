class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        p1 = 0
        p2 = 1
        while(p1<len(arr) and p2<len(arr)):
            if arr[p1]>arr[p2]:
                wins = wins + 1
                p2 = p2 + 1
            else:
                temp = p2+1
                p1= p2
                p2 = temp 
                wins = 1
            
            if wins==k:
                return arr[p1]
        
        return arr[p1]

