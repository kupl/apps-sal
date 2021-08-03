class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # k = minSize
        # count = collections.Counter(s[i:i + k] for i in range(len(s) - k + 1))
        # return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
        cnt = Counter()
        for size in range(minSize, maxSize + 1):
            for i in range(len(s) - size + 1):
                ss = s[i:i + size]
                if len(set(ss)) <= maxLetters:
                    cnt[ss] += 1
        return max(cnt.values()) if cnt else 0

        # sliding window
#         res = collections.Counter()
#         n = len(s)
#         size = minSize
#         while size <= maxSize:
#             M = collections.defaultdict(int)
#             for i, c in enumerate(s):
#                 if i < size:
#                     M[c] += 1
#                     continue

#                 if len(M) <= maxLetters:
#                     res[s[i-size:i]] += 1

#                 # slide the window
#                 M[s[i-size]] -= 1
#                 if M[s[i-size]] == 0:
#                     del M[s[i-size]]
#                 M[c] += 1
#             # check for last one
#             if len(M) <= maxLetters:
#                 res[s[n-size:]] += 1

#             size += 1

#         # print(res.most_common(1))
#         ans = res.most_common(1)
#         if not ans:
#             return 0
#         else:
#             return ans[0][1]
