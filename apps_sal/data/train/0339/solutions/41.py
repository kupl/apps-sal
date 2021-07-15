class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        Type1=dict()
        Product1=dict()
        Type2=dict()
        Product2=dict()
        for i in range(len(nums1)):
            product= nums1[i]*nums1[i]
            if product in Product1.keys():
                Product1[product]+=1
            else:
                Product1[product]=1
            for j in range(i+1, len(nums1)):
                new_product=nums1[i]*nums1[j]
                if new_product in Type1.keys():
                    Type1[new_product]+=1
                else:
                    Type1[new_product]=1
        for i in range(len(nums2)):
            product= nums2[i]*nums2[i]
            if product in Product2.keys():
                Product2[product]+=1
            else:
                Product2[product]=1
            for j in range(i+1, len(nums2)):
                new_product=nums2[i]*nums2[j]
                if new_product in Type2.keys():
                    Type2[new_product]+=1
                else:
                    Type2[new_product]=1
        res=0
        for i in Product1.keys():
            if i in Type2.keys():
                res+=Product1[i]*Type2[i]
        for i in Product2.keys():
            if i in Type1.keys():
                res+=Product2[i]*Type1[i]
        return res
