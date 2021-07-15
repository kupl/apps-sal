from sortedcontainers import SortedList
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        zeros = SortedList()
        zeros.add(0)
        zeros.add(len(arr) + 1)
        if len(arr) == m:
            return len(arr)
        for inverse_step, i in enumerate(arr[::-1], 1):
            head = zeros.bisect_left(i)
            # print(zeros, i, zeros.bisect_left(i), zeros.bisect_right(i))
            if  i - zeros[head - 1] - 1 == m:
                print((len(arr), inverse_step))
                return len(arr) - inverse_step
            
            tail = zeros.bisect_right(i)
            if  zeros[tail] - i - 1 == m:
                # print(len(arr), inverse_step)
                return len(arr) - inverse_step
            
            zeros.add(i)
        return -1
                
        
        
#         def is_length_existed(string):
#             last_zero = -1
#             for i, bit in string:
#                 if bit == 1:
#                     continue
#                 ones = i - last_zero
#                 if ones == m:
#                     return True
#                 last_zero = i
#             return False
        
#         def build(t):
#             string = [0] * len(arr)
#             for i in arr[:t]:
#                 string[i-1] = 1
        
#         p, q = 1, len(arr)
#         while p < q:
#             mid = (p + q) >> 1
#             string = build(mid)
#             if is_length_existed(string):
#                 p = mid
#             else:
#                 q = mid - 1
            
            
            
                    

