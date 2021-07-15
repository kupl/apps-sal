class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        def match(m1, m2):
            prod = 0
            for r1, r2 in zip(m1, m2):
                for v1, v2 in zip(r1, r2):
                    prod += v1 * v2
            return prod
        
        pad = [0] * (3 * (len(A) - 1))
        largeA = [pad] * (len(A) - 1)
        for i in range(len(A)):
            largeA.append([0] * (len(A)-1) + A[i] + [0] * (len(A)-1))
        largeA += [pad] * (len(A) - 1)
        maxProd = 0
        #print(largeA)
        for i in range(len(largeA) - len(A) + 1):
            for j in range(len(largeA) - len(A) + 1):
                subA = []
                for r in largeA[i:len(A) + i]:
                    subA.append(r[j:len(A) + j])
                prod = match(subA, B)
                if prod > maxProd:
                    maxProd = prod
        return maxProd
            
            
                

