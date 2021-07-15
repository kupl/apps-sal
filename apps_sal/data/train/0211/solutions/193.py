class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 1

        def func(string: str, visited: set):
            if string in visited or len(string) == 0:
                return 0
            res = 1
            for i in range(len(string)):
                s = string[:i + 1]
                if s in visited:
                    continue
                visited.add(s)
                temp = func(string[i + 1:], visited) + 1
                visited.remove(s)
                res = max(res, temp)

            return res

        return func(s, set())
