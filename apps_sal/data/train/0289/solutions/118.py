class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        la = []
        ma = []
        i = 0
        for i in range(len(A) - L + 1):
            la.append(sum(A[i:i+L]))
        for i in range(len(A) - M + 1):
            ma.append(sum(A[i:i+M]))
        print((la, ma))
        maxi = 0
        for i in range(len(la)):
            for j in range(len(ma)):
                if i < j:
                    if i + L > j:
                        continue
                if j < i:
                    if j + M > i:
                        continue
                if j == i:
                    continue
                maxi = max(maxi, la[i]+ma[j])
                        
        return maxi
            
        

