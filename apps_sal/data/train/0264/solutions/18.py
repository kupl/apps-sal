from typing import List


class Solution:

    def uniqueLength(self, string: str) -> int:
        for i in range(len(string)):
            if string.count(string[i]) > 1:
                return -1
        else:
            return len(string)

    def maxUnique(self, arr: List[str], index: int, curr_string: str, result: List[int]) -> List[int]:
        if index == len(arr) and self.uniqueLength(curr_string) > result[0]:
            result[0] = len(curr_string)
            return
        if index == len(arr):
            return
        self.maxUnique(arr, index + 1, curr_string, result)
        self.maxUnique(arr, index + 1, curr_string + arr[index], result)

    def maxLength(self, arr: List[str]) -> int:
        result = [0] * 1
        self.maxUnique(arr, 0, '', result)
        return result[0]
