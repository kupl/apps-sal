class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # 第一遍傻傻 两次循环TLE
        # 还是应该用stack, 单调递减栈 小的入栈
        
        res = 0
        stack = []
        for i, a in enumerate(A):
            if not stack or stack[-1][1] > a: # 小于才入栈， 相等就可以取res了
                stack.append((i,a))
            else:
                N = len(stack) -1  # 要遍历每一个入stack的
                while N >= 0 and stack[N][1]<= a:
                    res = max(res,i-stack[N][0])
                    N = N -1
                    
        return res

