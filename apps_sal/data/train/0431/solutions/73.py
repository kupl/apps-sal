class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        m = 10 ** 9 + 7
        prev_stack = []
        next_stack = []
        
        prev_smaller = {}
        next_smaller = {}
                
        for i in range(len(A)):
            while len(next_stack) > 0 and A[next_stack[-1]] >= A[i]:
                idx = next_stack.pop()
                next_smaller[idx] = i
                
            next_stack.append(i)
            
        while len(next_stack) != 0:
            idx = next_stack.pop()
            next_smaller[idx] = len(A)
    
        for i in range(len(A) - 1, -1, -1):
            while len(prev_stack) > 0 and A[prev_stack[-1]] > A[i]:
                idx = prev_stack.pop()
                prev_smaller[idx] = i
                
            prev_stack.append(i)
            
        while len(prev_stack) != 0:
            idx = prev_stack.pop()
            prev_smaller[idx] = -1
        
        # print(prev_smaller)
        # print(next_smaller)
        
        result = 0
        for i in range(len(A)):
            left_count = i - prev_smaller[i] - 1
            right_count = next_smaller[i] - i - 1
            num_occurrences = (left_count + 1) * (right_count + 1)
            result = (result + num_occurrences * A[i]) % m
            
        return result

