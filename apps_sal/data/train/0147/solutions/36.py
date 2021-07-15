from heapq import heappush, heappop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ## based on the hints
        ## since The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers
        ## we process engineer one by one in desceding order of his efficiency
        ## and keep track the running sum of the previous k largest speeds
        
        ## two priority queues
        M = 10**9+7
        eff_pq = [] ## max heap
        sp_pq = [] ## min heap
        speed_sum = 0 ## track the sum of largest k speeds
        ## push all efficiency and indexes into a max-heap
        for idx, eff in enumerate(efficiency):
            heappush(eff_pq, (-eff, idx))
        
        res = 0
        while len(eff_pq)>0:
            neg_eff, idx = heappop(eff_pq) ## process engineer one by one in desceding order of his efficiency
            eff = -neg_eff
            heappush(sp_pq, speed[idx]) ## push his speed into min-heap
            speed_sum += speed[idx] ## keep tracking the running sum
            
            ## maintain the priority queue with size <= k
            if len(sp_pq) > k:
                sp_pop = heappop(sp_pq)
                speed_sum -= sp_pop ## keep tracking the running sum
                
            ## note that a team be at most k engineers, which mean it can be less than k
            res = max(res, eff*speed_sum) 
            
        return res % M
# 6
# [2,10,3,1,5,8]
# [5,4,3,9,7,2]
# 2
# 3
# [2,8,2]
# [2,7,1]
# 2    

