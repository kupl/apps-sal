class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        ownhat = {}
        n = len(hats)
        maxhat = -1
        for i in range(n):
            hat = hats[i]
            for h in hat:
                maxhat = max(h, maxhat)
                if(h in ownhat):
                    ownhat[h].append(i)
                else:
                    ownhat[h] = [i]
        dp = [[-1 for i in range(pow(2, n))] for i in range(41)]

        @lru_cache(None)
        def dfs(ind, peoplemask):
            if(peoplemask == pow(2, n) - 1):
                return 1
            if(ind > maxhat):
                return 0
            count = 0
            count = dfs(ind + 1, peoplemask)
            if(ind in ownhat):
                for people in ownhat[ind]:
                    if(peoplemask & (pow(2, people)) == 0):
                        count = (count + dfs(ind + 1, peoplemask | pow(2, people))) % (pow(10, 9) + 7)
            return count
        return dfs(1, 0)
