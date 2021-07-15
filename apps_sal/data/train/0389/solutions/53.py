class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        dp = set([(0,0)])
        suma = sum(A)
        N = len(A)
        A.sort()
        for num in A:
            for k, v in list(dp):
                if k>=N//2: continue
                if num+v>suma*(k+1)//N: continue
                # print(k, v, num, dp)    
                if num+v==suma*(k+1)//N and suma*(k+1)%N==0 and k+1<N:
                    return True

                dp.add((k+1, num+v))
        
        return False


