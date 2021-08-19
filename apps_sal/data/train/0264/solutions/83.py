class Solution:

    def is_unique(self, s):
        return len(set(s)) == len(s)

    def maxLength(self, arr: List[str]) -> int:

        dct = {}
        maxVal = 0

        for i in range(0, len(arr)):
            if self.is_unique(arr[i]):
                v = frozenset(arr[i])

                dct[v] = len(v)
                maxVal = max(maxVal, len(v))

            for j in range(i + 1, len(arr)):
                t = arr[i] + arr[j]
                val = frozenset(t)

                if val not in dct.keys():
                    if self.is_unique(t):
                        # print(t)
                        arr.append(t)
                        dct[val] = len(val)
                        maxVal = max(maxVal, len(val))
        print(dct)
        return maxVal
