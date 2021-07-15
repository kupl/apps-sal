class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def no_of_days(weights,W,D):
            count=1
            su=0
            i=0
            while i<len(weights):
                if su+weights[i]<=W:
                    su+=weights[i]
                    i+=1
                else:
                    su=weights[i]
                    i+=1
                    count+=1
            # print(count)
            return count
        
        
        def binary(weight,i,j,D):
            ans=0
            while i<=j:
                mid=int((i+j)/2)
                d=no_of_days(weight,mid,D)
                # print(\"d=\", d, i, \" \", j, \" \", mid)
                if d<=D:
                    ans=mid
                    j=mid-1
                else:
                    i=mid+1
                    
            return ans
        
        wi=max(weights)
        wj=wi*len(weights)
        a=binary(weights,wi,wj,D)
        
        return a
                
                
                
            
            

