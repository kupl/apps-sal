from collections import Counter


class Solution:
    def dfs(self, arr, cur):
        for i, string_set in enumerate(arr):
            if cur.intersection(string_set):
                continue
            nxt = cur.union(string_set)
            nxt_key = ''.join(sorted(nxt))
            if nxt_key not in self.visited:
                self.visited.add(nxt_key)
                self.ans = max(self.ans, len(nxt))
                self.dfs(arr[:i] + arr[i:], nxt)

    def maxLength(self, arr: List[str]) -> int:

        # N is length of arr, K is longest str item in arr

        # filter and setify O(NK) time and space
        new_arr = []
        for string in arr:
            string_set = set(string)
            if len(string_set) == len(string):
                new_arr.append(string_set)
        arr = new_arr

        # recursive build O(?) with visited O(?) space
        self.visited = set()
        self.ans = 0
        self.dfs(arr, set())
        return self.ans
