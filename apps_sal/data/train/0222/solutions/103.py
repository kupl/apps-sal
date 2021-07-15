class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        length = len(A)
        s = set(A)
        result = 0
        for i in range(length-1):
            
            for j in range(i+1, length):
                a=A[i]
                b=A[j]
                count = 2
                while a+b in s:
                    a,b = b,a+b
                    count+=1
                result = max(result, count)

        return result if result > 2 else 0
