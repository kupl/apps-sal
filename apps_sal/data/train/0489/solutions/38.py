class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # ans = 0
        # m = float('inf')
        # for i in sorted(range(len(A)), key = A.__getitem__):
        #     m = min(i, m)
        #     ans = max(ans, i - m)
        # return ans
        stack = []
        # A.append(float('inf'))
        ans = 0
        for i, a in enumerate(A):
            if (not stack) or stack[-1][0] > a:
                stack.append((a, i))
            else:
                l, r = 0, len(stack) - 1
                while l < r:
                    # print(l, r)
                    m = (r + l) // 2
                    if stack[m][0] > a:
                        l = m + 1
                    else:
                        r = m
                    
                if stack[l][0] <= a:
                    ans = max(ans, i - stack[l][1])
            # print(stack, ans)
        return ans
                        
                        
                    
       
        


