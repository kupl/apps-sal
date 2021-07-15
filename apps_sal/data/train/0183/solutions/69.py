class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        L1=len(nums1)
        L2=len(nums2)
        temp=[[u*v for v in nums2] for u in nums1]
        dic={}
        dic[(0,0)]=temp[0][0]
        def search(i,j):
            if (i,j) in dic:
                return dic[(i,j)]
            if i==0:
                dic[(0,j)]=max(search(0,j-1),temp[0][j])
                return dic[(i,j)]
            elif j==0:
                dic[(i,0)]=max(search(i-1,0),temp[i][0])
                return dic[(i,0)]
            else:
                dic[(i,j)]=max(search(i-1,j), search(i,j-1), temp[i][j]+search(i-1,j-1), temp[i][j])
                return dic[(i,j)]
        return search(L1-1,L2-1)
