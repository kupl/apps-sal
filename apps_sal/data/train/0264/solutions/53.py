class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def unique_char_count(s):
            chars = set()
            for char in s:
                if char in chars:
                    return -1
                else:
                    chars.add(char)
            return len(s)

        def max_unique(arr, index, cur_str, result):
            if index >= len(arr):
                if unique_char_count(cur_str) > result[0]:
                    result[0] = len(cur_str)
                return
            max_unique(arr, index + 1, cur_str + arr[index], result)
            max_unique(arr, index + 1, cur_str, result)

        result = [0]
        max_unique(arr, 0, '', result)
        return result[0]
