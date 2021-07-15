class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # sm = sum(nums)
        # strt = sm//threshold
        
        # search_space = list(range(max(strt,1),sm))
        # n = len(search_space)
        l = 1
        r = max(nums)
        while(l+1<r):
            mid = l+(r-l)//2
            
            # if self.search(nums,search_space[mid],threshold)  == 0:
            #     return search_space[mid]
            if self.search(nums,mid,threshold) > 0:
                r = mid
            elif self.search(nums,mid,threshold) < 0:
                l = mid
        
        # print(search_space[l],search_space[r])
        if self.search(nums,l,threshold) >= 0:
            return l
        else:
            return r
        # print(search_space[l],search_space[r])
            
        
            
            
    def search(self,nums,i,threshold):
    
        insum = sum([math.ceil(el/i) for el in nums])
        # print(i,insum)
        
        # if insum == threshold:
        #     return 0
        if insum <= threshold:
            return 1
        else:
            return -1
            

