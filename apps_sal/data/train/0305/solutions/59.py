class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        ans = set([])
        for i in range(n):
            pat = text[i:]
            lps = [0] * (n - i)
            j = 1
            k = 0
            while j < len(lps):
                if pat[j] == pat[k]:
                    k += 1
                    lps[j] = k
                    j += 1
                    d = j - k
                    if j % d == 0 and j // d % 2 == 0:
                        ans.add(pat[:j])
                elif k != 0:
                    k = lps[k - 1]
                else:
                    lps[j] = 0
                    j += 1
        return len(ans)
