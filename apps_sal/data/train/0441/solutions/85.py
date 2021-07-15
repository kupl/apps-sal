class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
#         if N == 1: 
#             return 1
#         res = 1
#         for i in range(2, floor(1 + N ** (0.5))):   
#             if N % i == 0:
#                 if i % 2 == 1: # If i is odd, then we can form a sum of length i
#                     res += 1
#                 j = (N // i) # Check the corresponding N // i
#                 if i != j and j % 2 == 1:
#                     res += 1
#         if N % 2 == 1: # If N is odd(2k + 1). Then N = k + k + 1, not included above
#             res += 1
        
#         return res
        
#         if N == 1:
#             return 1
#         total = 1
        
#         start = 1
#         end = 1
        
#         curr = 1
#         while end <= ceil(N / 2):
#             if curr == N:
#                 total += 1
#                 curr -= start
#                 start += 1
#             if curr < N:
#                 end += 1
#                 curr += end
#             elif curr > N:
#                 curr -= start
#                 start += 1
        
#         return total
    
        def summer(x):
            return x * (x - 1) / 2
        count = 0
        i = 1
        
        while summer(i) < N:
            if ((N - summer(i)) %i == 0):
                count += 1
            i += 1
        return count
