class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n_arr = len(arr)
        if n_arr == 0:
            return -1
        
        def get_minlen_ending_before(array: List[int]) -> List[int]:
            n_array = len(array)
            minlen_array = [float('inf')] * n_array
            curr_sum = array[0]
            i = 0
            j = 0
            min_len = float('inf')
            while i < n_array and j < n_array:
                increment_i = False
                increment_j = False
                if curr_sum == target:
                    min_len = min(min_len, j - i + 1)
                    curr_sum -= array[i]
                    increment_i = True
                elif curr_sum < target:
                    increment_j = True
                    if j < n_array - 1:
                        curr_sum += array[j+1]
                elif curr_sum > target:
                    curr_sum -= array[i]
                    increment_i = True
                if j < n_array - 1:
                    minlen_array[j+1] = min_len
                if increment_i:
                    i += 1
                if increment_j:
                    j += 1
                if j < i and i < n_array:
                    j = i
                    curr_sum = array[i]
            return minlen_array
        
        prefix = get_minlen_ending_before(arr)
        postfix = (get_minlen_ending_before(arr[::-1] + [0])[1:])[::-1]
        
        min_sum = float('inf')
        for i in range(n_arr):
            min_sum = min(min_sum, prefix[i] + postfix[i])
        return min_sum if min_sum < float('inf') else -1
