class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        pairs1 = []
        pairs2 = []
        for i in range(n):
            for j in range(i + 1, n):
                pairs2.append(nums2[i] * nums2[j])
        for i in range(m):
            for j in range(i + 1, m):
                pairs1.append(nums1[i] * nums1[j])
        pairs1.sort()
        pairs2.sort()
        if len(pairs1) == 0 or len(pairs2) == 0:
            return 0

        def bs1(arr, key):
            if arr[0] > key:
                return -1
            if arr[-1] < key:
                return -1
            lo = 0
            hi = len(arr) - 1
            left = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] < key:
                    lo = mid + 1
                elif arr[mid] == key:
                    left = mid
                    hi = mid - 1
                else:
                    hi = mid - 1
            return left

        def bs2(arr, key):
            if arr[0] > key:
                return -1
            if arr[-1] < key:
                return -1
            lo = 0
            hi = len(arr) - 1
            right = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] < key:
                    lo = mid + 1
                elif arr[mid] == key:
                    right = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return right
        ans = 0
        for i in nums1:
            sq = i * i
            left = bs1(pairs2, sq)
            right = bs2(pairs2, sq)
            if left == -1:
                continue
            ans += right - left + 1
        for i in nums2:
            sq = i * i
            left = bs1(pairs1, sq)
            right = bs2(pairs1, sq)
            if left == -1:
                continue
            ans += right - left + 1
        return ans
