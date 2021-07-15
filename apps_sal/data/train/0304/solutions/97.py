class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        d={}
        ans=0
        
        for age in ages:
            if(age not in d):
                d[age]=1
            else:
                d[age]+=1
        
        print (d)
        for ageA,countA in (list(d.items())):
            for ageB ,countB in (list(d.items())):
                print((ageA,countA,ageB,countB))
                
                if(ageA*0.5+7>=ageB):
                    continue
                    
                if(ageA<ageB):
                    continue
                    
                if(ageA<100<ageB):
                    continue
                    
                if(ageA!=ageB):
                    ans+=countA*countB
                else:
                    ans+=(countA-1)*countA
                # if(ageA==ageB):
                #     ans-=countA
        return ans
                    

