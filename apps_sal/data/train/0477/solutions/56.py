class Solution:  
    def invert(s):
        inv_s = ''
        for char in s:
            if char == '1':
                inv_s += '0'
            else:
                inv_s += '1'

        return inv_s
    
    answer = ['0']
    
    for i in range(1, 21):
        prev_s = answer[i-1]
        answer.append(prev_s + '1' + invert(prev_s)[::-1])
        
    
    def findKthBit(self, n: int, k: int) -> str:
        
#         def invert(s):
#             inv_s = ''
#             for char in s:
#                 if char == '1':
#                     inv_s += '0'
#                 else:
#                     inv_s += '1'

#             return inv_s
        
#         result = ['0']
        
#         for i in range(1, 21):
#             prev_s = result[i-1]
#             # print(self.invert(prev_s))
#             result.append(prev_s + '1' + invert(prev_s)[::-1])
#             # break
            
        return self.answer[n-1][k-1]

