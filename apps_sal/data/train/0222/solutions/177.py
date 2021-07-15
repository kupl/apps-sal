class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        setA = set(A)
        answer = 0
        max_ = A[-1]
        visited = set()
        for i in range(len(A)-1):
            curr1 = A[i]
            for j in range(i+1, len(A)):
                curr2 = A[j]
                if (curr1, curr2) in visited:
                    continue
                visited.add((curr1, curr2))
                sum_ = curr1 + curr2
                l = 2 if sum_ in setA else 0
                while sum_ in setA and sum_ <= max_:
                    curr1, curr2 = curr2, sum_
                    sum_ = curr1 + curr2
                    visited.add((curr1, curr2))
                    l += 1

                answer = max(answer, l)
                curr1 = A[i]
        
        return answer
