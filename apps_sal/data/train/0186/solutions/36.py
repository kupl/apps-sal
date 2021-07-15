class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
       
        for i in range(len(cost)):
            for j in range(len(cost)-1, i, -1):
                if cost[j] and not cost[i]%cost[j]:
                    cost[i] = 0
                    break
        costMap = {e: k+1 for k,e in enumerate(cost) if e}
        print((costMap, cost))
        def getMaxList(s1, s2):
            if s2 == None: return ''
            return ''.join(sorted(s1+s2, reverse = True))
              
        def dfs(c):
           
            if c in dp: return dp[c]
            if c == 0: return ''
            elif c < 0: return None
            # print(c)
           
            strs = [getMaxList(str(i), dfs(c-cost[i-1])) for i in range(1,10) if cost[i-1] in costMap]
            if not any(strs): 
                dp[c] = None
                return None
            l = max(list(map(len, strs)))
            newStr = sorted(strs)
            for i in range(len(strs)-1, -1, -1):
                if len(newStr[i]) == l:
                    dp[c] = newStr[i]
                    return dp[c]
        dp = {}
        res = dfs(target)
        return res if res else '0'

