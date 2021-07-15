import copy
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def dfs(temp, s, res):
            if len(s) == 0:
                if len(''.join(list(set(temp)))) == n and len(temp) > len(res):
                    res = copy.deepcopy(temp)
                return res
            for i in range(1, len(s) + 1):
                
                temp.append(s[:i])
                # print(temp)
                res = dfs(temp, s[i:], res)
                temp.pop()
            return res
        
        return len(dfs([], s, []))

