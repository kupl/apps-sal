class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1.sort()
        # nums2.sort()
        count = 0
        for i in range(len(nums1)):
            target = nums1[i]**2
            temp = defaultdict(int)
            for j in range(len(nums2)):
                if (target / nums2[j]) in list(temp.keys()):
                    count += temp[target / nums2[j]]
                temp[nums2[j]] += 1

        for i in range(len(nums2)):
            target = nums2[i]**2
            temp = defaultdict(int)
            for j in range(len(nums1)):
                if (target / nums1[j]) in list(temp.keys()):
                    count += temp[target / nums1[j]]
                temp[nums1[j]] += 1
        # for i in range(len(nums1)):
        #     s2=nums1[i]**2
        #     first,last=0,len(nums2)-1
        #     while nums2[last//2]>s2:
        #         last//=2+1
        #     while first<last:
        #         if nums2[first]*nums2[last]==s2:
        #             count+=1
        #             break
        #         elif nums2[first]*nums2[last]>s2:
        #             last-=1
        #         else:
        #             first+=1
        # for i in range(len(nums2)):
        #     s2=nums2[i]**2
        #     first,last=0,len(nums1)-1
        #     while nums1[last//2]>s2:
        #         last//=2+1
        #     while first<last:
        #         if nums1[first]*nums1[last]==s2:
        #             count+=1
        #             break
        #         elif nums1[first]*nums1[last]>s2:
        #             last-=1
        #         else:
        #             first+=1
        return count
