class Solution:
    def maxLength(self, arr: List[str]) -> int:
        possible_strings = ['']
        maximum = 0
        for i in range(len(arr)):
            temp_len = len(possible_strings)
            for j in range(temp_len):
                x = arr[i] + possible_strings[j]
                if (len(x) == len(set(x))):
                    possible_strings.append(x)
                    maximum = max(maximum, len(x))
        return maximum
