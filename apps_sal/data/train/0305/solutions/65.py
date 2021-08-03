class Solution:
    def checkSymetric(self, checkString):
        l = len(checkString)
        if l % 2 != 0 or l == 0:
            return False

        if checkString[:l // 2] != checkString[l // 2:]:
            return False
        return True

    def distinctEchoSubstrings(self, text: str) -> int:
        l = len(text)
        dic = {}
        for start in range(l):
            for end in range(l, start, -1):
                if (end - start) % 2 == 0:
                    if (self.checkSymetric(text[start:end])):
                        dic[text[start:end]] = 1
        return len(list(dic.keys()))
