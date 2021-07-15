from collections import defaultdict as dt
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        fi = dt(int)
        for i in letters:
            fi[i] += 1
        ans = 0
        for j in range(1,len(words)+1):
            tt = list(combinations(words, j))
            print(tt)
            for i in tt:
                ss = 0
                if ch(fi,i):
                    for k in i:
                        ss+= sc(k,score)
                    ans = max(ss,ans)
        return ans
def sc(w,z):
    s = 0
    for i in w:
        s+=z[ord(i)-97]
    return s

def ch(fi,s):
    gi = dt(int)
    for i in s:
        for j in i:
            gi[j] += 1
    for i in gi:
        if gi[i]>fi[i]: return False
    return True
