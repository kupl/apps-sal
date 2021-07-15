class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def helper(i,s,seen):
            if i > len(s)-1:
                return len(seen)
            max_len = 1
            for k in range(i,len(s)):
                temp = set(seen)
                temp.add(s[i:k+1])
                max_len = max(max_len, helper(k+1, s,temp))
            return max_len
        return helper(0,s,set([]))

