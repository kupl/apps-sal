class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # subStrCounter = Counter()
        # subStrCounter[1] = text[0]
        # l = 0
        # r = 1
        ans = 0
        visited = set()
        textLen = len(text)
        for i in range(textLen - 1):
            for j in range(0, min(i + 1, textLen - i - 1)):
                if text[i - j:i + 1] == text[i + 1:i + j + 2]:
                    if text[i - j:i + 1] not in visited:
                        visited.add(text[i - j:i + 1])
                        ans += 1
                # if text[i-j] == text[i+j+1]:
                #     if text[i+1: i+j+2] not in visited:
                #         visited.add(text[i+1: i+j+2])
                #         ans += 1
                # else:
                #     break
        return ans
