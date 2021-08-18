class Solution:

    def is_unique(self, s):
        return len(set(s)) == len(s)

    def maxLength(self, arr: List[str]) -> int:

        dct = {}
        maxVal = 0

        for i in range(0, len(arr)):
            v = frozenset(arr[i])
            if self.is_unique(arr[i]):
                maxVal = max(maxVal, len(v))

            for j in range(i + 1, len(arr)):
                t = arr[i] + arr[j]
                val = frozenset(t)

                if self.is_unique(t):
                    arr.append(t)
                    maxVal = max(maxVal, len(val))
        return maxVal
