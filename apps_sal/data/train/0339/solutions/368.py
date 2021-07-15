class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def cal(arr1, arr2):
            countMap = {}
            m = defaultdict(list)
            count = 0
            for i in range(len(arr2)): m[arr2[i]].append(i)
            for e in arr1:
                if e in countMap: 
                    count += countMap[e]
                    continue
                c = 0
                for i in range(len(arr2)):
                    if not e*e%arr2[i]:
                        d = e*e//arr2[i]
                        c += sum([0]+[1 for idx in m[d] if idx != i])
                countMap[e] = c
                count += c
                        
            return count//2
        return cal(nums1, nums2) + cal(nums2, nums1)
