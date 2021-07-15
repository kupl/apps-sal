from functools import lru_cache

p = 10**9 +7 
class Solution:
    
#     def get_number_of_ways(self, hats, mask, p_id): #p_id = person_id
#         if p_id>=len(hats):
#             return 1
        
#         if dp[p_id].get(mask, None):
#             return dp[p_id][mask]
#         else:
#             dp[p_id][mask] = 0
        
#         for i in hats[p_id]:
#             if (mask & (1<<i))>>i :
#                 continue
#             temp_mask = mask | (1<<i)
#             val = self.get_number_of_ways(hats, temp_mask, p_id+1)
#             if val == -1:
#                 continue
            
#             dp[p_id][mask] += val
        
#         return dp[p_id][mask]

        
    def numberWays(self, hats):
        max_hat_id = 0
        distinct_hats = set()
        for person_hats in hats:
            for i in range(len(person_hats)):
                person_hats[i] -= 1
                distinct_hats.add( person_hats[i])
        hat_id_mapping = dict()
        i = 0
        for hat in distinct_hats:
            hat_id_mapping[hat] = i
            i += 1
            
        persons = [[] for i in range(len(distinct_hats))]
        
        for p_id in range(len(hats)):
            for hat_id in hats[p_id]:
                persons[hat_id_mapping[hat_id]].append(p_id)
        dp = dict()
        for i in range(len(persons)):
            dp[i]= dict()
        allmask = (1<<len(hats))-1
        
        def get_number_of_ways( mask, hat_id): #p_id = person_id
            if mask == allmask :
                return 1
            if hat_id>=len(persons):
                return 0
            
            if (hat_id, mask) in dp:
                return dp[(hat_id, mask)]
            else:
                dp[(hat_id, mask)] = get_number_of_ways( mask, hat_id+1)
            for i in persons[hat_id]:
                if (mask & (1<<i))>>i :
                    continue
                temp_mask = mask | (1<<i)
                val = get_number_of_ways( temp_mask, hat_id+1)
                
                dp[(hat_id, mask)] += val
            
            return dp[(hat_id, mask)]
            
        
        ans = get_number_of_ways( 0, 0)
        return ans%p
        
        
        
        
        
        # @lru_cache(None)
#         def get_number_of_ways( mask, hat_id, allmask): #p_id = person_id
#             if mask == allmask :
#                 return 1
#             if hat_id>=len(persons):
#                 return 0
            
#             if dp[hat_id].get(mask, None):
#                 return dp[hat_id][mask]
#             else:
#                 dp[hat_id][mask] = get_number_of_ways( mask, hat_id+1, allmask)
#             for i in persons[hat_id]:
#                 if (mask & (1<<i))>>i :
#                     continue
#                 temp_mask = mask | (1<<i)
#                 val = get_number_of_ways( temp_mask, hat_id+1, allmask)
                
#                 dp[hat_id][mask] += val
            
#             return dp[hat_id][mask]
            
        
        
#         return get_number_of_ways( 0, 0, allmask) % p

