class Solution:

    def longestOnes(self, arr: List[int], k: int) -> int:
        (start, max_length) = (0, 0)
        count_0 = 0
        for end in range(len(arr)):
            if arr[end] == 0:
                count_0 += 1
            while count_0 > k:
                if arr[start] == 0:
                    count_0 -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
