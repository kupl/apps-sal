class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 10:04
        # arr2=list(set(arr2))
        arr2.sort()
        # we might need fix at point 0
        # hence we will always compare it will

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
                # arr1 is increasing, we have reached so far
                return 0
            else:
                ans = float('inf')
                if arr1[i] > prev:
                    # no need of replacement
                    ans = min(ans, helper(i + 1, j, arr1[i]))
                    # pick any index from arr2 starting j
                idx = bsearch(j, len(arr2) - 1, prev)
                if idx != -1:
                    ans = min(ans, 1 + helper(i + 1, idx + 1, arr2[idx]))


#                 for k in range(j,len(arr2)):
#                     # can we use binary search here
#                     # we got to find out the minumum value in arr2 which is greater than prev

#                     if arr2[k]>prev:
#                         # we can probably use binary search here
#                         # get the first index which is strictly greater than prev
#                         ans=min(ans,1+helper(i+1,k+1,arr2[k]))
#                         break
                return ans
        ans = helper(0, 0, -1)
        return -1 if ans == float('inf') else ans
