class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0

        def walk(i, temp):
            self.res = max(self.res, len(temp))

            for j in range(i, len(arr)):
                if all(v <= 1 for v in list(collections.Counter(temp + arr[j]).values())):
                    walk(j + 1, temp + arr[j])
            return

        walk(0, '')
        return self.res
