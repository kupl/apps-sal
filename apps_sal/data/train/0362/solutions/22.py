class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        h2p = collections.defaultdict(list)
        n = len(hats)
        MOD = 10**9 + 7

        for people, hat_list in enumerate(hats):
            for h in hat_list:
                h2p[h].append(people)

        def dp(hat, mask):
            if (hat, mask) in memo:
                return memo[(hat, mask)]
            if mask == (1 << n) - 1:
                return 1
            if hat > 40:
                return 0

            ans = dp(hat + 1, mask)
            if hat in h2p:
                peoples = h2p[hat]
                for p in peoples:
                    if mask & (1 << p) == 0:
                        ans += dp(hat + 1, mask | (1 << p))
                        # mask|=(1<<p)
                        # ans += dp(h+1,mask)
                        # mask ^= (1<<p)
            memo[(hat, mask)] = ans
            return ans

        memo = {}
        return dp(0, 0) % MOD


#         h2p = collections.defaultdict(list)
#         n = len(hats) # number of people

#         for people,hat_list in enumerate(hats):
#             for h in hat_list:
#                 h2p[h].append(people)

#         def dp(hat,mask): # hat index and people bit mask,  since n<=10,so use people as bitmask, otherwise if uses hat will TLE
#             if (hat,mask) in memo:return memo[(hat,mask)]

#             if mask == (1<<n)-1: # base case
#                 return 1
#             if h >40:return 0
#             # not use current hat
#             ans = dp(hat+1,mask)
#             # use current hat
#             if hat in h2p:
#                 peoples = h2p[hat]
#                 for p in peoples:
#                     if mask & (1<<p) == 0: # means this people has not assigned a hat yet
#                         mask |= (1<<p)
#                         ans += dp(hat+1,mask)
#                         mask ^= (1<<p)
#                         # ans += dp(hat+1,mask|(1<<p))
#             memo[(hat,mask)] = ans
#             return ans
#         memo = {}
#         return dp(0,0)
