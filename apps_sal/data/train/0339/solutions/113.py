class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find(A, target):
            # print(A, target)
            l, r = 0, len(A) - 1
            ans = 0
            while l < r:
                s = A[l] * A[r]
                if s == target:
                    i = l + 1
                    while i < r and A[i] == A[l]:
                        i += 1
                    numL = i - l
                    j = r - 1
                    while j > l and A[j] == A[r]:
                        j -= 1
                    numR = r - j
                    l = i
                    r = j
                    if i > j and A[i] == A[j]:
                        ans += (r - l) * (r - l - 1) // 2
                    else:
                        ans += numL * numR
                    # print(ans)
                elif s < target:
                    l += 1
                else:
                    r -= 1
            return ans
        
        ans = 0
        nums1.sort()
        nums2.sort()
        for n in nums1:
            ans += find(nums2, n * n)
        for n in nums2:
            ans += find(nums1, n * n)
        return ans
