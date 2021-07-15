class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # My First Solution
        widx = 0  # current winner index
        i = next((i for i,x in enumerate(arr) if x > arr[widx] and k>=i>0),None)
        if i: widx = i  
        else: return arr[widx] 
        
        while widx < len(arr):
            i=next((i for i,x in enumerate(arr) if x > arr[widx] and k>i-widx>0),None)
            if i: widx = i
            else: return arr[widx]
        
        # Clean Discussion Solution
        win = cnt = 0 #winner & count 
        for i, x in enumerate(arr): 
            if win < x: win, cnt = x, 0 #new winner in town 
            if i: cnt += 1 #when initializing (i.e. i == 0) count=0
            if cnt == k: break #early break 
        return win 
        

