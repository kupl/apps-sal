class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        currli = []
        visiting = set()
        self.maxval = 1
        def dfs(st, s):
            if len(s) <= 0:
                self.maxval = max(self.maxval, len(currli))
                return True
            # if i >= n:
            #     # currli.append(s)
            #     if s not in visiting:
            #         return True
            #     else:
            #         return False
                
            for i in range(1, len(s) + 1):
                # print(s[0:i], s)
                if s[0:i] not in visiting:
                    visiting.add(s[0:i])
                    currli.append(s[0:i])
                    dfs(i, s[i:])
                    # if dfs(i, s[i:]):
                    #     return True
                    currli.pop()
                    visiting.remove(s[0:i])
                
            return False
            
            
        
        
        for i in range(1, n+1):
            visiting.add(s[0:i])
            currli.append(s[0:i])
            # print(s[0:i], s[i:])
            dfs(i, s[i:])
            # if dfs(i, s[i:]):
            #     break
            currli.pop()
            visiting.remove(s[0:i])
            
        # return len(currli)
        return self.maxval

