class Solution:
    def minOperationsMaxProfit(self, a: List[int], bc: int, rc: int) -> int:
        max_pr = pr = 0; cnt = max_cnt = 0; w = 0; i = 0
        while i < len(a) or w > 0:
            x = w + a[i] if i < len(a) else w            
            pr += min(x, 4) * bc - rc                        
            cnt += 1            
            if pr > max_pr: max_pr, max_cnt = pr, cnt             
            w = max(x - 4, 0)      
            i += 1                          
        return max_cnt if max_pr > 0 else -1
