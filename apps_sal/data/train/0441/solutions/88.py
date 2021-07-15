# Idea1 - Brute force
# - start going down from N
# - ...
# 
# Idea2 - Recursion
# - start with N
# - then find two consequetive number that add to N
# - then try to break down each number
# 
# - may not work; see Example 2 & 3
# - need to find a way to divide (recursively or not) in different ways
# 
# Idea3 - Lower (2) and upper (N-1?)?
# - consider N combination as in
#   - divide N by 2, by 3, ..., M then somehow adjust each number
#     - whats the biggest number M can be
# 
# Idea4


class Solution:
    # def consecutiveNumbersSum(self, N: int) -> int:
    #     ret = 1
    #     m = 2
    #     while (N/m - floor(m/2) > 0):
    #         l = ceil(N/m) - floor(m/2)
    #         cur = [l + i for i in range(m)]
    #         print(cur)
    #         if (sum(cur) == N):
    #             ret += 1
    #         m += 1
    #     return ret
    
    def consecutiveNumbersSum(self, N: int) -> int:
        def consum(p):
            return p*(p+1)/2
        
        count = 0
        i = 1
        while consum(i) <= N:
            if (N - consum(i)) % i == 0:
                count += 1
            i += 1
        return count
