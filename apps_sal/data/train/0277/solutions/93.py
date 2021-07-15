class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        _max = 0
        _min = 1
        num_moments = 0
        for i in range(len(light)):
            if _max < light[i]:
                _max = light[i]
            
            if _max - _min == i:
                num_moments += 1
        return num_moments
#         _min = len(light)+1
#         _max = 0
#         missing = set()
#         num_moments = 0
        
#         for i in light:
#             if i > _max:
#                 if _max != 0:
#                     for j in range(_max+1, i):
#                         missing.add(j)
#                 _max = i
#             if i < _min:
#                 if _min != len(light)+1:
#                     for j in range(i+1, _min):
#                         missing.add(j)
#                 _min = i
#             if i in missing:
#                 missing.remove(i)
#             if len(missing) == 0 and _min < 2:
#                 num_moments+=1
#         return num_moments
                
        
#         number_of_moments = 0
#         max_seen_value = 0
#         min_seen_index = len(light)+1
        
#         for i in range(len(light)):
#             if abs(max_seen - light[i]) == 1 and min_seen_index == 0:
#                 number_of_moments += 1
            
#             if light[i] > max_seen:
#                 max_seen = light[i]-1
            
#             if min_seen_index < light[i] - 1:
#                 min_seen_index == light[i] - 1
            
            
#         return number_of_moments 
    
    
    # max = 3, index = 2
    # max = 3, index = 1
    # max = 4, index = 1
    # max = 4, index = 0
    
    
#     light_on = [0]*len(light)
#         number_of_moments = 0
#         farthest_pos = 0
#         for i in range(len(light)):
#             all_blue = True
#             light_on[light[i]-1] = 1
#             if light[i] - 1 > farthest_pos:
#                 farthest_pos = light[i] - 1
#             for j in range(farthest_pos):
#                 if light_on[j] == 0:
#                     all_blue = False
#                     break;
#             if all_blue:
#                 number_of_moments += 1
            
#         return number_of_moments  

