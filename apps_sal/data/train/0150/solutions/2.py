class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        a = [A[0]]
        b = [0 for i in range(len(A))]
        for i in range(1, len(A)):
            a.append(max(a[i - 1], A[i]))
        
        b[-1] = A[-1]
        for i in range(len(A) - 2, -1, -1):
            b[i] = min(b[i + 1], A[i])
            
        for i in range(len(A) - 1):
            if a[i] <= b[i + 1]:
                return i + 1
        return -1
