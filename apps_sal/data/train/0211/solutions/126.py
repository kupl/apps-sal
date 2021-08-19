class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s) - 1
        ans = 1
        for i in range(2**n + 1):
            prev = 0
            ok = True
            visited = set()
            for j in range(n):
                if i & (1 << j):
                    tmp = s[prev:j + 1]
                    prev = j + 1
                    if tmp in visited:
                        ok = False
                        break
                    visited.add(tmp)
                    # print(visited)
                if not ok:
                    break
            if not ok:
                continue
            tmp = s[prev:]
            #print(tmp, visited)
            if tmp not in visited:
                # print(visited)
                ans = max(ans, len(visited) + 1)
        return ans
