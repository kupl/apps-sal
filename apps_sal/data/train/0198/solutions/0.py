class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        dist = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

#         i = 0
#         cur = 0
#         res = 0
#         for j in range(len(s)):
#             cur += dist[j]
#             while cur>maxCost:
#                 cur -= dist[i]
#                 i += 1
#             res = max(res, j-i+1)

#         return res

        i = 0
        cost = maxCost
        for j in range(len(s)):
            cost -= dist[j]
            if cost < 0:
                cost += dist[i]
                i += 1

        return j - i + 1
