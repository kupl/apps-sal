class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        '''
        result=set()
        i=0
        j=1

        while(i<len(s)):
            if s[i:j] not in result:
                if s[j:len(s)] in result:
                    result.add(s[i:])
                    break
                elif s[i:j]==s[j:len(s)]:
                    result.add(s[i:])
                    break
                else:
                    result.add(s[i:j])
                    i=j
                    j=i+1
            else:
                j+=1
        return len(result)
        '''
        seen = set()
        n = len(s)

        def dfs(i):
            if i == n:
                return 0
            res = 1
            for j in range(i + 1, n + 1):
                if s[i:j] not in seen and s[j:] not in seen and s[i:j] != s[j:]:
                    seen.add(s[i:j])
                    res = max(res, dfs(j) + 1)
                    seen.remove(s[i:j])
            return res
        return dfs(0)
