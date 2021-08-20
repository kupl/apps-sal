class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        def bsearch(left, right, val):
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr2[mid] > val:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        @lru_cache(None)
        def helper(i, j, prev):
            if i >= len(arr1):
                return 0
            else:
                ans = float('inf')
                if arr1[i] > prev:
                    ans = min(ans, helper(i + 1, j, arr1[i]))
                idx = bsearch(j, len(arr2) - 1, prev)
                if idx != -1:
                    ans = min(ans, 1 + helper(i + 1, idx + 1, arr2[idx]))
                return ans
        ans = helper(0, 0, -1)
        return -1 if ans == float('inf') else ans
