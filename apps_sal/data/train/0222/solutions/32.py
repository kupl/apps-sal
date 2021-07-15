class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        mp = {}
        
        for v in A:
            mp[v] = set()
        
        result = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                l = 2
                while True:
                    if b in mp[a]:
                        break
                    if l != 2:
                        mp[a].add(b) 
                    c = a + b
                    if c not in mp:
                        break
                    a, b = b, c
                    l += 1
                if l < 3:
                    l = 0
                else:
                    result = max(result, l)
        return result

