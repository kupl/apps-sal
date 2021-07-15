class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        return self.recursion(A, B, {})
        
    def recursion(self, A: str, B: str, memo: dict) -> int:

        if A == '':
            return 0
        
        key = A + ',' + B
        if key in memo:
            return memo[key]
        
        if A[0] == B[0]:
            return self.recursion(A[1:], B[1:], memo)
        
        move = 100000
        for i in range(1, len(A)):
            if B[i] == A[0]:
                tempB = B[1:i] + B[0] + B[i + 1:]
                move = min(move, self.recursion(A[1:], tempB, memo))

        memo[key] = move + 1
        return 1 + move
