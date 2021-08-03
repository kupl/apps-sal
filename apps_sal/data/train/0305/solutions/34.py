class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        n = len(text)
        for sz in range(1, int(n / 2) + 1, 1):
            r = sz
            cur = 0
            for l in range(0, n - sz):
                if text[l] == text[r]:
                    cur += 1
                else:
                    cur = 0
                if cur == sz:
                    #print('size: ' + str(sz) + ' L: ' + str(l) + text[l-sz:l])
                    res.add(text[l - sz + 1:l + 1])
                    cur -= 1
                r += 1
        return len(res)
