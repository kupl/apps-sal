class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ln_s = len(s)
        ans = 0
        seen = Counter()
        for i in range(ln_s):
            set_buff = set(s[i:i + minSize])
            for j in range(i + minSize - 1, min(ln_s, i + maxSize)):
                buff = s[i:j + 1]
                set_buff.add(s[j])
                if len(set_buff) > maxLetters:
                    break
                seen[buff] += 1
                ans = max(ans, seen[buff])
        return ans
