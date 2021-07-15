class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        num_set = set(A)
        used = set()
        
        max_len = 2
        for x in range(len(A)):
            a = A[x]
            for y in range(x+1, len(A)):
                i, j = a, A[y]

                if (i, j) not in used:
                    used.add((i, j))
                    count = 2
                    while i+j in num_set:
                        count += 1
                        i, j = j, i+j
                        used.add((i, j))
                        
                    max_len = max(count, max_len)
        return 0 if max_len == 2 else max_len
            

