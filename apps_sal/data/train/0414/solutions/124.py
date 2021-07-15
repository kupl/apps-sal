class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win = cnt = 0 #winner & count 
        for i, x in enumerate(arr): 
            if win < x: win, cnt = x, 0 #new winner in town 
            if i: cnt += 1 #when initializing (i.e. i == 0) count is 0
            if cnt == k: break #early break 
        return win 
