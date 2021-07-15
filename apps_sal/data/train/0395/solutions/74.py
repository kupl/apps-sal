class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        
        next_higher = [0 for x in range(n)] 
        next_lower = [0 for x in range(n)]
        stack = []
        
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
            

        higher = [0 for x in range(n)] 
        lower = [0 for x in range(n)]
        higher[-1] =  1
        lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
