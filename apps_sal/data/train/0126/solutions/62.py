from collections import defaultdict
from collections import Counter


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = defaultdict(int)
        for i in range(len(s)):
            for j in range(i + minSize - 1, min(i + maxSize, len(s))):
                sub = s[i:j + 1]
                if len(set(sub)) <= maxLetters:
                    dic[sub] += 1
        if len(dic):
            return max(dic.values())
        else:
            return 0
