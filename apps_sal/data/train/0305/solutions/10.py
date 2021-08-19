class Solution:

    def checkValid(self, checkString):
        l = len(checkString)
        if l % 2 != 0 or l == 0:
            return False
        if checkString[:l // 2] != checkString[l // 2:]:
            return False
        return True

    def distinctEchoSubstrings(self, text: str) -> int:
        l = len(text)
        dic = {}
        if l == 0:
            return 0
        for start in range(l - 1):
            for end in range(l, start, -1):
                diff = end - start
                left = text[start:diff // 2 + start]
                right = text[diff // 2 + start:end]
                if diff > 0 and diff % 2 == 0 and (left == right):
                    dic[text[start:end]] = 1
        return len(list(dic.keys()))
