
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
        # Try to merge [0..i] from the left into [r..n-1]. If it doesn't work, 
        # push r forward and try again, until we run out of either room for i to expand
        # toward the right or for r to push forward to the right.
        i = 0
        while i < l + 1:
            if arr[i] <= arr[r]:
                min_to_remove = min(min_to_remove, r - i - 1)
                i += 1
            elif r < n - 1:
                r += 1
                # i += 1 # More intuitive and less subtle to NOT increment i

                # Why? Because if after i gets incremented a few times to
                # i' such that arr[i'] <= arr[r], then arr[r] must be >=
                # all elements in [i..i'-1] because elements in [0..l] are
                # non-decreasing. In other words as soon we hit line 
                # `if arr[i] <= arr[r]:` (after incrementing i a few times
                # without successfully finding some arr[r], arr[i] <= arr[r]),
                # all those values behind arr[i] can now be included in the merged
                # result.
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
        
        

        
        

