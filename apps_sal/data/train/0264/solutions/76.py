from collections import Counter


class Solution:

    def maxLength(self, arr) -> int:
        if len(arr) == 1:
            return len(arr[0])
        self.max_val = 0
        max_val = float('-inf')

        def check(string):
            c = Counter(string)
            for (key, val) in c.items():
                if c[key] > 1:
                    return False
            return True

        def _helper(string, index):
            if check(string):
                self.max_val = max(self.max_val, len(string))
            else:
                return
            if index >= len(arr):
                return
            for i in range(index, len(arr)):
                newString = string + arr[i]
                _helper(newString, i + 1)
        print(_helper('', 0))
        return self.max_val
