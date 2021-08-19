class Solution:

    def lastSubstring(self, s: str) -> str:
        ind = collections.defaultdict(list)
        for i in range(len(s)):
            ind[s[i]].append(i)
        maxy = max(ind)
        ans = ''
        off = 0
        for i in ind[maxy]:
            s = s[i - off:]
            off += i - off
            ans = max(ans, s)
        return ans
