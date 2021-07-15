class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Find the longest monotonically non-decreasing prefix array in [0, i]
        n = len(arr)
        l = 1
        while l < n and arr[l-1] <= arr[l]:
            l += 1
        l -= 1  
        if l >= n - 2:
            return n - 1 - l
                
        # Find the longest monotonically non-decreasing suffix array in [j, n - 1]
        r = n - 2
        while r >= 0 and arr[r] <= arr[r+1]:
            r -= 1
        r += 1
        if r <= 1:
            return r
    
        # Start off with min of either left or right side removed as the min_to_move
        min_to_remove = min(n - 1, n - 1 - (l + 1) + 1, r)
        # Try to merge [0..i] from the left into [r..n-1]. We start with assuming
        # entire right side [r..n-1] could be included and try to see if [0], [0, 1] and so on
        # from the left side could be merged in. Until we hit some i on the left side that is 
        # too large for the current arr[r], retreat r back further to the right to try
        # against a bigger value. Keep trying until we run out of either room for i to expand
        # toward the right or for no more r left to retreat to the right.
        i = 0
        while i < l + 1:
            if arr[i] <= arr[r]:
                min_to_remove = min(min_to_remove, r - i - 1)
                # we could definitely include arr[i] into the result
                i += 1
            elif r < n - 1:
                # We cannot include arr[r] into the result but we could
                # include arr[i] into the result
                r += 1
                i += 1
            else:
                break
        
        return min_to_remove

        
    def findLengthOfShortestSubarray_bruteforce_bsearch(self, arr: List[int]) -> int:
        # Returns the smallest index `idx` such that arr[idx] >= val
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
        
        # Find the longest monotonically non-decreasing prefix array in [0, i]
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
                
        # Find the longest monotonically non-decreasing suffix array in [j, n - 1]
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
        
        # For each value arr[k], in [0, i], find the `right_idx` into the suffix array in [j, n - 1]
        # such that arr[k] >= arr[right_idx]. We want to find the one that results in the longest
        # sequence [0..k] + [right_idx..n-1]
        min_to_remove = float('inf')
        for k in range(i, -1, -1):
            right_idx = bsearch(arr[k], j, n - 1)
            l = k + 1 + n - right_idx
            to_remove = n - l
            min_to_remove = min(min_to_remove, to_remove)
            
        # For each value arr[k], in [j, n-1], find the `left_idx` into the prefix array in [0, i]
        # such that arr[k] >= arr[left_idx - 1]. We want to find the one that results in the longest
        # sequence [0..left_idx-1] + [k..n-1]
        for k in range(j, n):
            left_idx = bsearch(arr[k], 0, i)
            l = left_idx + n - k
            to_remove = n - l
            min_to_remove = min(min_to_remove, to_remove)
        
        return min_to_remove
        
        

        
        

