class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        a = [k // 26 for _ in range(27)]

        for i in range(k % 26 + 1):
            a[i] += 1

        ns, nt = len(s), len(t)
        if ns != nt:
            return False

        for i in range(ns):
            if s[i] == t[i]:
                continue
            else:
                d = ord(t[i]) - ord(s[i]) if t[i] > s[i] else ord(t[i]) + 26 - ord(s[i])
                if a[d] <= 0:
                    return False
                a[d] -= 1

        return True
