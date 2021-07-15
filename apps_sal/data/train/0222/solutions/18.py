class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        count = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                temp = 2
                a = A[i]
                b = A[j]
                while a+b in s:
                    temp += 1
                    count = max(count, temp)
                    t = a
                    a = b
                    b = t+b
        return count
                    

