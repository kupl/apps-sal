class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        count = self.counttrip(nums1, nums2)

        count += self.counttrip(nums2, nums1)
        return int(count)

    def counttrip(self, nums1, nums2):
        seen = defaultdict(int)
        count = 0
        for i in nums1:
            p = i * i
            if(p in seen):
                count += seen[p]
                continue

            localcount = 0
            left = 0
            right = len(nums2) - 1

            while(left < right):
                if(nums2[left] > p):
                    break
                if(nums2[left] * nums2[right] == p):
                    if(nums2[left] == nums2[right]):
                        n = right - left + 1
                        localcount += n * (n - 1) / 2
                        break
                    localcount += 1
                    nleft = left + 1
                    while(nums2[nleft] == nums2[nleft - 1] and nleft < right):
                        nleft += 1
                        localcount += 1
                    right -= 1
                    left = 0
                elif(nums2[left] * nums2[right] > p):

                    right -= 1
                elif(nums2[left] * nums2[right] < p):
                    left += 1
            count += localcount
            seen[p] = localcount

        return count
