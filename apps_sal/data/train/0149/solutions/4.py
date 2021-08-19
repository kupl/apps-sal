class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        unique = set(s)
        dups = []

        for c in unique:
            dups.append(c * k)

        while True:
            start = s
            for c in dups:
                s = s.replace(c, '')

            if start == s:
                return s

#         ret = list(s)

#         while True:
#             s = ret
#             ret = []
#             ac = 1
#             for c in s:
#                 if not ret or ret[-1] != c:
#                     ac = 1
#                     ret.append(c)
#                 else:
#                     if ac + 1 == k:
#                         while ac:
#                             ret.pop()
#                             ac -= 1
#                     else:
#                         ret.append(c)
#                         ac += 1
#                 # print(ret, ac)
#             if len(ret) == len(s):
#                 break

#         return ''.join(ret)
