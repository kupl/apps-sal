class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        B = [0]+A+A
        for i in range(1, len(B)):
            B[i] += B[i-1]
        maxv = B[1]
        
        stack = deque([0])
        for end in range(1, len(B)):
            num = B[end]
            while stack and num < B[stack[-1]]:
                stack.pop()
            stack.append(end)
            if end-stack[0] == n+1:
                stack.popleft()
            maxv = max(num-B[stack[0]], maxv)
            #print(end, stack, maxv)
        if all(x<0 for x in A):
            return max(A)
        return maxv
                
                

