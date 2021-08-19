from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, r = 0, 0
        d = defaultdict(int)
        res = 0

        for r in range(len(tree)):
            d[tree[r]] += 1
            while len(d) > 2:
                # print(l)
                d[tree[l]] -= 1
                if d[tree[l]] == 0:
                    d.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
            # print(r,l)

        return res

#         while r < len(tree):

#             while len(d) <= 2:
#                 r += 1
#                 if r < len(tree):
#                     d[tree[r]] += 1
#                 else:
#                     break

#             if len(d) > 2 or r == len(tree):
#                 res = max(res, r - l)

# #            print(\"1s\", r, l)

#             while len(d) > 2:
#                 d[tree[l]] -= 1
#                 if d[tree[l]] == 0:
#                     d.pop(tree[l])
#                 l += 1

# #            print(\"2s\", r, l)
#         return res
