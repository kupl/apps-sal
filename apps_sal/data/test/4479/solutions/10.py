class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        result = 0
        count = 0
        A.sort()
       
        if A[0] > 0:
            if K%2 == 1:
                A[0] = -A[0]
            for i in A:
                result += i
            return(result)
        elif A[0] == 0:
            for i in A:
                result += i
            return(result)
        else:
            for j in range (len(A)):
                if A[j] >= 0:
                    break
                else:
                    count += 1
            ra = K%count
            if K < count:
                for m in range(K):
                    A[m] = -A[m]
            else:
                for m in range(count):
                    A[m] = -A[m]
                K -= count
                A.sort()
                if K%2 == 1:
                    A[0] = -A[0]
            for i in A:
                result += i
            
            return(result)
