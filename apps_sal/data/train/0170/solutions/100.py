
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 1
        while l < n and arr[l - 1] <= arr[l]:
            l += 1
        l -= 1
        if l >= n - 2:
            return n - 1 - l

        r = n - 2
        while r >= 0 and arr[r] <= arr[r + 1]:
            r -= 1
        r += 1
        if r <= 1:
            return r

        min_to_remove = min(n - 1, n - 1 - (l + 1) + 1, r)
        i = 0
        while i < l + 1:
            if arr[i] <= arr[r]:
                min_to_remove = min(min_to_remove, r - i - 1)
                i += 1
            elif r < n - 1:
                r += 1

            else:
                break

        return min_to_remove

    def findLengthOfShortestSubarray_bruteforce_bsearch(self, arr: List[int]) -> int:
        def bsearch(val, low, high):
            while low < high:
                mid = (low + high) // 2
                if arr[mid] >= val:
                    high = mid
                else:
                    low = mid + 1
            if val > arr[high]:
                return high + 1
            return high

        n = len(arr)
        curr_max = float('-inf')
        i = 0
        while i < n:
            if arr[i] < curr_max:
                break
            curr_max = arr[i]
            i += 1
        i -= 1
        if i >= n - 2:
            return n - 1 - i

        curr_min = float('inf')
        j = n - 1
        while j >= 0:
            if arr[j] > curr_min:
                break
            curr_min = arr[j]
            j -= 1
        j += 1
        if j <= 1:
            return j

        min_to_remove = float('inf')
        for k in range(i, -1, -1):
            right_idx = bsearch(arr[k], j, n - 1)
            l = k + 1 + n - right_idx
            to_remove = n - l
            min_to_remove = min(min_to_remove, to_remove)

        for k in range(j, n):
            left_idx = bsearch(arr[k], 0, i)
            l = left_idx + n - k
            to_remove = n - l
            min_to_remove = min(min_to_remove, to_remove)

        return min_to_remove
