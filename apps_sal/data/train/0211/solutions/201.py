class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.cnt = 0

        def getstring(start, visited):
            if start == len(s):
                self.cnt = max(self.cnt, len(visited))
                return

            for end in range(start + 1, len(s) + 1):
                temp = s[start:end]
                if temp in visited:
                    continue
                visited.add(temp)
                getstring(end, visited)
                visited.remove(temp)
        getstring(0, set())
        return self.cnt
