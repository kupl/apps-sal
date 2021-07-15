class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo={}
        def counter(start, last, last_count, left):
            if (start, last, last_count, left) in memo:
                return memo[(start, last, last_count, left)]
            if left<0:
                return sys.maxsize
            if start>=len(s):
                return 0
            
            if s[start]==last:
                incre=1 if last_count==1 or last_count==9 or last_count==99 else 0
                memo[start, last, last_count, left]=incre+counter(start+1, last, last_count+1, left)
            else:
                keep=1+counter(start+1, s[start], 1, left)
                delete=counter(start+1, last, last_count, left-1)
                memo[start, last, last_count, left]=min(keep, delete)
            return memo[start, last, last_count, left]
        return counter(0, '', 0, k)
