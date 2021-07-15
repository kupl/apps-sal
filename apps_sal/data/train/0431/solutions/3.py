class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # build previous less element array
        previous_less = [-1] * len(A)
        p_stack = []
        
        # build next less element array
        next_less = [len(A)] * len(A)
        n_stack = []
        
        for i in range(len(A)):
            n = A[i]
            # remove larger until find the smaller one
            while p_stack and A[p_stack[-1]] > n:
                p_stack.pop()
            # stack top is previous less of A[i]
            # if empty, record -1, else record stack top index
            if p_stack:
                previous_less[i] = p_stack[-1]
            else:
                previous_less[i] = -1
            p_stack.append(i)
            
            # remove larger until find the smaller one
            while n_stack and A[n_stack[-1]] > n:
                # index of the one need to be updated
                # the one that is bigger than A[i]
                x = n_stack[-1]
                n_stack.pop()
                next_less[x] = i
            n_stack.append(i)
            
        #print(previous_less)
        #print(next_less)
        
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(len(A)):
            # calculate distance to left and right
            left = i - previous_less[i]
            right = next_less[i] - i
            #print(left)
            #print(right)
            
            ans = (ans + A[i] * left * right) % mod
        return ans
