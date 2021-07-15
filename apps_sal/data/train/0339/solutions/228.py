class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1={}
        d2={}
        for i in nums1:
            d1[i]=d1.get(i,0)+1
        for i in nums2:
            d2[i]=d2.get(i,0)+1
        ans=0
        d3={}
        print(d1,d2)
        for i in range(len(nums1)):
            d3={}
            for j in range(len(nums2)):
                if (nums1[i]*nums1[i])%nums2[j]==0:
                    #print(1,nums1[i],nums2[j])
                    x=(nums1[i]*nums1[i])//nums2[j]
                    y=nums2[j]
                    if d3.get((x,y),-1)==-1:
                        if x==y:
                            x1=d2.get(x,0)
                            ans+=(x1*(x1-1))//2
                            d3[(x,y)]=1
                        else:    
                        #print(1,d2,(nums1[i]*nums1[i])//nums2[j])
                            ans+=d2.get(x,0)*d2.get(y,0) 
                            #d2[nums2[j]]+=1
                            d3[(x,y)]=1
                            d3[(y,x)]=1
        d4={}
        for i in range(len(nums2)):
            d4={}
            for j in range(len(nums1)):
                if (nums2[i]*nums2[i])%nums1[j]==0:
                    #d1[nums1[j]]-=1
                    x=((nums2[i]*nums2[i])//nums1[j])
                    y=nums1[j]
                    if d4.get((x,y),-1)==-1:
                        #print(2,nums2[i],nums1[j])
                        #print(2,d1,((nums2[i]*nums2[i])//nums1[j]))
                        if x==y:
                            x1=d1.get(x,0)
                            ans+=(x1*(x1-1))//2
                            d4[(x,y)]=1
                        else:    
                            ans+=d1.get(x,0)*d1.get(y,0) 
                            #d1[nums1[j]]+=1
                            d4[(x,y)]=1
                            d4[(y,x)]=1
        return ans
