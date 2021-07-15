class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        ans = 1
        N = 1
        flags = [0]*K
        while (1):
            red = N % K
            if red == 0:
                return ans
            elif flags[red] > 0:
                return -1
            else:
                flags[red] += 1
            
            N = N * 10 + 1
            ans += 1

