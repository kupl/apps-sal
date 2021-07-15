from collections import defaultdict
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = defaultdict(int)
        for i in range(0, len(s) - minSize + 1):
            for j in range(minSize, maxSize + 1):
                if i + j > len(s):
                    break
                cur_str = s[i:i+j]

                unique_letters = set(cur_str)
                if len(unique_letters) > maxLetters:
                    continue
                else:
                    dic[cur_str] += 1


        res = 0
        for s in dic:
            res = max(res, dic[s])
        return res
