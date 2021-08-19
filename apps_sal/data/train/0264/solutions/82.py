from collections import Counter


class Solution:

    def maxLength(self, arr: List[str]) -> int:
        max_str = 0
        for i in range(len(arr)):
            if self.is_unique(arr[i]) and len(arr[i]) > max_str:
                max_str = len(arr[i])
            concat = [arr[i]]
            for j in range(i + 1, len(arr)):
                for x in concat:
                    c = x + arr[j]
                    if self.is_unique(c):
                        if len(c) > max_str:
                            max_str = len(c)
                        concat.append(c)
        return max_str

    def is_unique(self, str):
        for v in Counter(str).values():
            if v > 1:
                return False
        return True
