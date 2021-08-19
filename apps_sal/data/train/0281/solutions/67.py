class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        visited = {}
        for (ss, tt) in zip(s, t):
            if ss != tt:
                d = (ord(tt) - ord(ss)) % 26
                if d not in visited:
                    visited[d] = d
                else:
                    visited[d] += 26
                if visited[d] > k:
                    return False
        return True
