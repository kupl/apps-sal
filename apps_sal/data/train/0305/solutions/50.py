class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        l = len(text)
        dic = {}
        if l == 0:
            return 0
        for start in range(l - 1):
            for end in range(l, start, -1):
                diff = end - start
                if diff % 2 == 0 and text[start:diff // 2 + start] == text[diff // 2 + start:end]:
                    dic[text[start:end]] = 1
        return len(list(dic.keys()))
