class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newarr = []
        for cur in arr:
            newarr.append(collections.Counter(cur))
        res = [0]

        def helper(cur, index):
            if index == len(arr):
                res[0] = max(res[0], len(cur))
            else:
                if len(arr[index]) == len(newarr[index]) and not newarr[index] & cur:
                    helper(newarr[index] + cur, index + 1)
                helper(cur, index + 1)

        helper(collections.Counter(''), 0)

        return res[0]
