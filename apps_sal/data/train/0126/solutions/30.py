import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans, freq_subs, n = collections.defaultdict(int), 0, len(s)
        for i in range(n - minSize + 1):
            for j in range(i + minSize, n + 1):
                if len(set(s[i: j])) <= maxLetters:
                    if s[i:j] in ans:
                        ans[s[i:j]] += 1
                        freq_subs = max(freq_subs, ans[s[i:j]])
                    else:
                        ans[s[i:j]] = 1
                        freq_subs = max(freq_subs, 1)
                else:
                    break
        return freq_subs
