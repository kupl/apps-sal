class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        start_index = 0
        longest_ones = 0
        max_length = 0
        for end_index in range(len(arr)):
            if arr[end_index] == 1:
                longest_ones += 1
            if longest_ones + k <= (end_index - start_index):
                if arr[start_index] == 1:
                    longest_ones -= 1
                start_index += 1
            max_length = max(max_length, end_index - start_index + 1)
        return max_length
