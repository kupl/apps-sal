class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        result = 0
        string_set = set()
        n = len(text)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (j - i) % 2:
                    continue
                s0 = text[i:j]
                if s0 in string_set:
                    continue
                string_set.add(s0)
                s1 = text[i:i + (j - i) // 2]
                s2 = text[i + (j - i) // 2:j]
                if s1 == s2:
                    result += 1
        return result
