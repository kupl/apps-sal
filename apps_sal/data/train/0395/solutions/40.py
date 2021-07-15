class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        sorted_enums = sorted(enumerate(A), key = lambda x:x[1])
        for i, c in sorted_enums:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        
        sorted_enums = sorted(enumerate(A), key = lambda x:-x[1])
        stack = []
        for i, c in sorted_enums:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        
        dp_higher, dp_lower = [0] * n, [0] * n
        dp_higher[n-1] = 1
        dp_lower[n-1] = 1
        
        for i in range(n-2, -1, -1):
            dp_higher[i] = dp_lower[next_higher[i]]
            dp_lower[i] = dp_higher[next_lower[i]]

        return sum(dp_higher)
