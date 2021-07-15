class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max_satisfaction = 0
        for i in range(0, len(satisfaction)):
            curr_satisfaction = 0
            timestamp = 1
            for j in range(i, len(satisfaction)):
                curr_satisfaction += satisfaction[j] * timestamp
                timestamp += 1
            max_satisfaction = max(max_satisfaction, curr_satisfaction)
        return max_satisfaction
            
#         cache = {}
#         def maxSatisfactionHelper(satisfaction, start, timestamp):
#             if not satisfaction:
#                 return 0
            
#             if (start,timestamp) in cache:
#                 return cache[(start, timestamp)]
            
#             max_satisfaction = 0
            
#             max_satisfaction = max((satisfaction[0] * timestamp) +                           maxSatisfactionHelper(satisfaction[1:], start+1, timestamp + 1), 
#                                   maxSatisfactionHelper(satisfaction[1:], start+1, timestamp))
            
#             cache[(start, timestamp)] = max_satisfaction
#             return max_satisfaction
        
#         return maxSatisfactionHelper(sorted(satisfaction), 0, 1)
            

