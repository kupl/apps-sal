class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum1=sum(A)
        if sum1%3!=0:
            return False
        
        else:
            div=sum1//3
            print(div)
            i1,sum2=0,0
            for i in A:
                sum2=sum2+i
                print(sum2,i)
                if sum2==div:
                    i1=i1+1
                    print('sum2',sum2)
                    sum2=0
            if i1>=3 and div==0:
                return True
            if i1==3:
                return True
            return False
