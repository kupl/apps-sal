class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        n, seen = len(s), set()
        for i in range(n):
            for j in range(i + 2, n + 1, 2):
                tmp = s[i:j]
                l = (j - i) // 2
                if tmp[:l] == tmp[l:]:
                    seen.add(tmp[:l])

        return len(seen)
