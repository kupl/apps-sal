class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        temp_arr = []
        temp_count = 0
        for n in nums:
            if n % 2 != 0:
                temp_arr.append(temp_count)
                temp_count = 0
            else:
                temp_count = temp_count + 1

        temp_arr.append(temp_count)
        if len(temp_arr) - 1 < k:
            return 0
        i = k - 1
        count = 0
        while i < len(temp_arr) - 1:
            start_len = temp_arr[i - k + 1] + 1
            end_len = temp_arr[i + 1] + 1
            count = count + (start_len * end_len)
            i = i + 1
        return count
