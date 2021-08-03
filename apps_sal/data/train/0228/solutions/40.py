class Solution:
    def maxVowels(self, s, k):
        vcnt, res = dict(), 0
        for i, c in enumerate(s):
            if i - k >= 0 and s[i - k] in 'aeiou':
                vcnt[s[i - k]] -= 1
            if c in 'aeiou':
                vcnt[c] = vcnt.get(c, 0) + 1
            #res = max(res, sum(vcnt.values()))
            if sum(vcnt.values()) > res:
                res = sum(vcnt.values())
        return res

# class Solution:
#     def maxVowels(self, s, k):
#         res, cnt = 0, 0
#         for i, c in enumerate(s):
#             if i-k >= 0 and s[i-k] in 'aeiou':
#                 cnt -= 1
#             if c in 'aeiou':
#                 cnt += 1
#             #res = max(res, cnt)
#             if cnt > res: res = cnt
#         return res

# class Solution:
#     def maxVowels(self, s, k):
#         cnt, res, N = 0, 0, len(s)
#         for i, c in enumerate(s[:k]):
#             if c in 'aeiou':
#                 cnt += 1
#         res = cnt
#         for c1, c2 in zip(s[:-k], s[k:]):
#             cnt += (c2 in 'aeiou') - (c1 in 'aeiou')
#             #res = max(res, cnt)
#             if cnt > res: res = cnt
#         return res
