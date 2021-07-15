class Solution:
    def formMulitplication(s, a):
        # a should have been sorted in ascending order 
        n=len(a)
        square_nums=[]
        for i in range(n-1):
            for j in range(i+1, n):
                p=a[i]*a[j]
                sqrt_p=int(sqrt(p))
                if sqrt_p*sqrt_p==p:
                    square_nums.append(sqrt_p)
        return square_nums
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        countnums1=[0 for i in range(100000+1)]
        countnums2=[0 for i in range(100000+1)]
        
        for i in range(len(nums1)):
            countnums1[nums1[i]]+=1
        for i in range(len(nums2)):
            countnums2[nums2[i]]+=1
        
        square_nums1=self.formMulitplication(nums1)
        result_type1=0
        for i in range(len(square_nums1)):
            result_type1+=countnums2[square_nums1[i]]
        
        square_nums2=self.formMulitplication(nums2)
        result_type2=0
        for i in range(len(square_nums2)):
            result_type2+=countnums1[square_nums2[i]]
        
        return (result_type1+result_type2)

