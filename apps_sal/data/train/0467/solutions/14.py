class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum2=0
        for n in nums:
            cnt=0
            sum1=0
            for i in range(1,int(sqrt(n))+1):
                if n%i==0:
                    if i==sqrt(n):
                        cnt+=1
                    else:
                        cnt+=2
                        sum1+=i+n//i
            if cnt==4:
                sum2 += sum1
        return sum2

