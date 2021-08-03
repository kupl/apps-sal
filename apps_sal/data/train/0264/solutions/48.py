class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.max = 0

        def helper(idx, chars):
            if idx >= n:
                if len(chars) == len(set(chars)):
                    self.max = max(self.max, len(chars))
            else:
                helper(idx + 1, chars)
                # temp =
                # for c in arr[idx]:
                #     chars.append(c)
                helper(idx + 1, chars + list(arr[idx]))

        helper(0, [])
        return self.max
