from typing import List


class Solution:
    def helper(self, current, arr, index, chars, remaining):
        if index == len(arr):
            return current
        maxLength = current
        for i in range(index, len(arr), 1):
            remaining -= len(arr[i])
            if current + len(arr[i]) + remaining <= maxLength:
                continue
            isGood = True
            for c in arr[i]:
                if c in chars:
                    isGood = False
                    break
            if isGood:
                for c in arr[i]:
                    chars.add(c)
                maxLength = max(self.helper(current + len(arr[i]), arr, i + 1, chars, remaining), maxLength)
                for c in arr[i]:
                    chars.remove(c)
        return maxLength

    def maxLength(self, arr: List[str]) -> int:
        arr = [a for a in arr if len(a) == len(set(a))]
        remaining = sum([len(a) for a in arr])
        return self.helper(0, arr, 0, set(), remaining)
