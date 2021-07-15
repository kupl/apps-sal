class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        count=self.counttrip(nums1,nums2)
        
        count+=self.counttrip(nums2,nums1)
        return int(count)
        
    def counttrip(self,nums1,nums2):
        
        count =0
        seen=defaultdict(int)
        for i in nums1:
            
            
            target=i*i
            # if(target in seen):
            #     count+=seen[target]
            #     continue
            localcount=0
            dictn=defaultdict(int)
            for j,x in enumerate(nums2):
                rem = target/x
                if(rem in dictn):
                    localcount+=dictn[rem]
                dictn[x]+=1
            seen[target]+=localcount
            count+=localcount
        return count
