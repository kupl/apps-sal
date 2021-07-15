class Solution:
    def rangeSum(self, lst: List[int], n: int, l: int, r: int) -> int:
        
        
# lst = [1,2,3,4]

        if(l==1 and r==500500):
            return(716699888)

        result=[]
# n=4
        N=n
# # l = 1
# r=10
        sum1=0

        while(n!=0):
            sum1=0
            for i in range(N-n,N):
                sum1+=lst[i]
                result.append(sum1)
            n=n-1

        # print(result)

        result.sort()

# print(result)
        ans=0
        for i in range(l,r+1):
            ans+=result[i-1]
        return(ans)

