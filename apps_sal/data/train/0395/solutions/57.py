class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n
        
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        
        validOddStartingPoints, validEvenStartingPoints = [0] * n, [0] * n
        validOddStartingPoints[-1] = validEvenStartingPoints[-1] = 1
        
        for i in range(n-2, -1, -1):
            validOddStartingPoints[i] = validEvenStartingPoints[next_higher[i]]
            validEvenStartingPoints[i] = validOddStartingPoints[next_lower[i]]
        
        return sum(validOddStartingPoints)
