class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ret = defaultdict(int)
        for i in range(len(s)):
            temp = ''
            char = set()
            for j in range(i, len(s)):
                temp = temp + s[j]
                char.add(s[j])
                if len(char) <= maxLetters and minSize <= len(temp) <= maxSize:
                    ret[temp] += 1
                elif len(char) > maxLetters or len(temp) > maxSize:
                    break

        if len(ret) == 0:
            return 0
        return max(ret.values())
