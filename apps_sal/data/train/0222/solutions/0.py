class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        def getFS(x1, x2):
            F = [x1, x2]
            while F[-1] <= 1000000000:
                F.append(F[-2] + F[-1])
            return F

        C1 = getFS(1, 0)
        C2 = C1[1:]
        
        def getLLFS(x1, x2):
            max_len = 2
            F = [x1, x2]
            xi = x1 + x2
            while xi in setA: 
                max_len += 1
                F.append(xi)
                xi = F[-2] + F[-1]
            if max_len == 6:
                print(F)
            return max_len
        
        max_len = 2
        setA = set(A)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x1, x2 = A[i], A[j]
                
                # calculate X_{max_len+1}
                if x1 * C1[max_len] + x2 * C2[max_len] > A[-1]:
                    break
                max_len = max(max_len, getLLFS(x1, x2))
                
        if max_len < 3:
            return 0
        return max_len
        

