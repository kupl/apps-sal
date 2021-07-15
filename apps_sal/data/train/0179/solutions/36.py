class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def backtrack(s, start, last, last_cnt, left, memo):
            if left < 0:
                return float('inf')
            
            if len(s) - start <= left:
                return 0
            
            if (start, last, last_cnt, left) in memo:
                return memo[(start, last, last_cnt, left)]
            
            ans = float('inf')
            if s[start] == last:
                if last_cnt == 1:
                    inc = 1
                else:
                    inc = len(str(last_cnt + 1)) - len(str(last_cnt))
                    
                ans = min(ans, inc + backtrack(s, start+1, last, last_cnt+1, left, memo))
            else:
                # delete
                delete_res = backtrack(s, start+1, last, last_cnt, left-1, memo)
                # keep
                keep_res = 1 + backtrack(s, start+1, s[start], 1, left, memo)
                
                ans = min(delete_res, keep_res)
                
            memo[(start, last, last_cnt, left)] = ans
            return memo[(start, last, last_cnt, left)]
        
        
        return backtrack(s, 0, '', 0, k, dict())
                

