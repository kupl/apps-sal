class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def fun(arr):
            res={}
            for i in range(len(arr)-1):
                for j in range(i+1,len(arr)):
                    if arr[i]*arr[j] in res.keys():
                        res[arr[i]*arr[j]] +=1
                    else:
                        res[arr[i]*arr[j]] =1
            return res
        
        x= fun(nums1)
        y= fun(nums2)
        res = 0
        for i in range(len(nums1)):
            if nums1[i]**2 in y.keys():
                print(nums1[i])
                res+=y[nums1[i]**2]
        
        for i in range(len(nums2)):
            if nums2[i]**2 in x.keys():
                res+=x[nums2[i]**2]
                       
        return res
