class Solution:

    def maxLength(self, arr: List[str]) -> int:
        return self.backtrack(set(), arr, 0)

    def backtrack(self, curr, arr, index):
        if index >= len(arr):
            return len(curr)
        max_len = 0
        for i in range(index, len(arr)):
            char_set = set([c for c in arr[i]])
            if curr.intersection(char_set) == set() and len(char_set) == len(arr[i]):
                curr = curr.union(char_set)
                max_len = max(max_len, self.backtrack(set(curr), arr, i + 1))
                curr = curr.difference(char_set)
            else:
                max_len = max(max_len, self.backtrack(curr, arr, i + 1))
        return max_len
