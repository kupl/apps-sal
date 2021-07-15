class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}
        
        def process(i, x, c, k):
            if not (i, x, c, k) in cache:
                ans = 101
                if i == -1:
                    return 0
                else:
                    # delete s[i]
                    if k > 0:
                        ans = min(ans, process(i-1, x, c, k-1))
                    # keep s[i]
                    if s[i] != x:
                        ans = min(ans, 1+process(i-1, s[i], 1, k))
                    elif c == 1 or c == 9 or c == 99:
                        ans = min(ans, 1+process(i-1, x, c+1, k))
                    else:
                        ans = min(ans, process(i-1, x, c+1, k))            
                
                cache[(i, x, c, k)] = ans
            return cache[(i, x, c, k)]
        
        n = len(s)
        return process(n-1, '*', 0, k)
