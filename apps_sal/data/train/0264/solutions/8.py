class Solution:
    def recurse(self, arr, cur):

        for i, x in enumerate(arr):
            if cur.intersection(x):
                continue
            nxt = cur.union(x)
            nxt_key = ''.join(sorted(nxt))
            if nxt_key not in self.visited:
                self.visited.add(nxt_key)
                self.maxlen = max(self.maxlen, len(nxt))
                self.recurse(arr[:i] + arr[i + 1:], nxt)

    def maxLength(self, arr: List[str]) -> int:

        # setify
        arr = [set(x) for x in arr if len(set(x)) == len(x)]

        self.maxlen = 0
        self.visited = set()
        self.recurse(arr, set())

        return self.maxlen
