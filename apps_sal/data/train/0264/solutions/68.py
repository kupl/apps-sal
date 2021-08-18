class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 1:
            return len(arr[0])

        self.res = 0

        def backtrack(start: int, path: set):
            self.res = max(self.res, len(path))

            if start == len(arr):
                return

            for i in range(start, len(arr)):
                new_chars = set(arr[i])
                if len(new_chars) != len(arr[i]):
                    continue

                if len(new_chars & path) == 0:
                    new_path = new_chars | path
                    backtrack(i + 1, new_path)

        backtrack(0, set())
        return self.res
