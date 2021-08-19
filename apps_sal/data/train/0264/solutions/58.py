class Solution:

    def maxLength(self, arr: List[str]) -> int:

        def valid(s, baskets):
            return all([c not in baskets for c in s])

        def find_max_len_recursive(baskets, currIdx):
            if currIdx == len(arr):
                return len(baskets)
            res1 = float('-inf')
            if valid(arr[currIdx], baskets):
                res1 = find_max_len_recursive(baskets.union(set(arr[currIdx])), currIdx + 1)
            res2 = find_max_len_recursive(baskets, currIdx + 1)
            return max(res1, res2)
        arr = [s for s in arr if len(s) == len(set(s))]
        return find_max_len_recursive(set(), 0)
