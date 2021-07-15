class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        avg = 0
        for i in A:
            avg += i
        if(avg%3 != 0): return False
        count = 0
        sum = 0
        for i in range(0,len(A)):
            if(sum == avg//3):
                if(i!=0):
                    count += 1
                    sum = A[i]
            elif(sum != avg//3):
                sum += A[i]
        if(sum == avg//3): count += 1
        return count >= 3
