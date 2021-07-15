class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        stack = []
        ans = dot = 0
        for idx, val in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= val:
                x,c = stack.pop()
                count += c
                dot -= x*c
            
            stack.append((val,count))
            dot += val * count
            ans += dot
        return ans % mod
