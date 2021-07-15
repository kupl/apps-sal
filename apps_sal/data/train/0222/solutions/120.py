class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        longest = 0
        coll = set(A)
        n = len(A)
        
        lookup = [[0 for _ in range(n)] for _ in range(n)] 
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if n - j + 1 < longest - lookup[i][j]:
                    break
                target = A[i] + A[j]
                prev = A[j]
                while target in coll:
                    if lookup[i][j]:
                        lookup[i][j] += 1
                    else:
                        lookup[i][j] = 3
                    temp = target
                    target += prev
                    prev = temp
                    longest = max(longest, lookup[i][j])
                    
        return longest
