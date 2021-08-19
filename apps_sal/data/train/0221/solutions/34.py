class Solution:

    def find(self, s, m):
        seen = collections.defaultdict(list)
        mod = 1 << 63 - 1
        base = 26
        d = pow(26, m - 1, mod)
        chal = 0
        for i in range(len(s)):
            if i >= m:
                l_chal = ord(s[i - m]) - ord('a')
                chal = (chal - l_chal * d) % mod
            l_chal = ord(s[i]) - ord('a')
            chal = (chal * base + l_chal) % mod
            if i >= m - 1:
                s_i = s[i - m + 1:i + 1]
                if chal in seen:
                    for j in seen[chal]:
                        s_j = s[j - m + 1:j + 1]
                        if s_j == s_i:
                            return s_i
                else:
                    seen[chal].append(i)
        return ''

    def longestDupSubstring(self, S: str) -> str:
        l = 2
        h = len(S) - 1
        ans = ''
        while l <= h:
            m = (l + h) // 2
            s = self.find(S, m)
            if s != '':
                ans = s
                l = m + 1
            else:
                h = m - 1
        return ans
