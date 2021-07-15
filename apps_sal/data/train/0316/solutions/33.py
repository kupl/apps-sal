class Solution:
    def longestPrefix(self, s: str) -> str:
        pre = self.get_pre(s)
        return s[0:pre[-1]]
        
    def get_pre(self, pattern):
        pre = [0]
        n = len(pattern)
        j = 0
        for i in range(1, n):
            while j and pattern[j] != pattern[i]:
                j = pre[j-1]
                
            if pattern[i] == pattern[j]:
                j +=1
            pre.append(j)
        return pre
