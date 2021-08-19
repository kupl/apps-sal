class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)

        u = list(range(len(arr) + 1))
        size = [0] * (len(arr) + 1)

        def find(a):
            if u[a] != a:
                u[a] = find(u[a])
            return u[a]

        def union(a, b):
            u1 = find(a)
            u2 = find(b)
            if u1 != u2:
                if size[u1] < size[u2]:
                    u[u1] = u2
                    size[u2] += size[u1]
                else:
                    u[u2] = u1
                    size[u1] += size[u2]
        ans = -1
        for a_idx, a in enumerate(arr):
            # print(a)
            # print(\"u\", u)
            # print(\"s\", size)
            size[a] = 1
            for i in [a - 1, a + 1]:
                if 1 <= i <= len(arr):
                    if size[find(i)] == m:
                        ans = a_idx
                    if size[i] > 0:
                        union(a, i)
                    # if size[find(a)] == m:
                    #     ans = a_idx+1

        # print(\"u\", u)
        # print(\"s\", size)

        for i in range(1, len(arr) + 1):
            # print(i, find(i))
            if size[find(i)] == m:
                return len(arr)
        # print(\"not last\")
        return ans

#         sections = [
#             [1, len(arr)]
#         ]
#         arr = arr[::-1]
#         for a_idx, a in enumerate(arr):
#             # print(a, sections)
#             l = 0
#             r = len(sections)
#             while l < r:
#                 c = l + (r-l)//2
#                 if sections[c][0] <= a <= sections[c][1]:
#                     # a at left
#                     if a == sections[c][0]:
#                         sections[c][0] = a+1
#                         if sections[c][0] > sections[c][1]:
#                             sections = sections[:c] + sections[c+1:]
#                         else:
#                             if sections[c][1] - sections[c][0] + 1 == m:
#                                 return len(arr) - a_idx - 1
#                     elif a == sections[c][1]:
#                         sections[c][1] = a-1
#                         if sections[c][0] > sections[c][1]:
#                             sections = sections[:c] + sections[c+1:]
#                         else:
#                             if sections[c][1] - sections[c][0] + 1 == m:
#                                 return len(arr) - a_idx - 1
#                     else:
#                         tmp = sections[c][1]
#                         sections[c][1] = a-1
#                         sections = sections[:c+1] + [[a+1, tmp]] + sections[c+1:]
#                         # heapq.heappush(sections, [a+1, tmp])
#                         if sections[c][1] - sections[c][0] + 1 == m:
#                             return len(arr) - a_idx - 1
#                         if sections[c+1][1] - sections[c+1][0] + 1 == m:
#                             return len(arr) - a_idx - 1
#                     break
#                 elif a < sections[c][0]:
#                     r = c
#                 elif a > sections[c][1]:
#                     l = c+1
#             # print(sections)

#         return -1

#         ans = -1
#         dp = [0] * (len(arr)+1)
#         for idx, a in enumerate(arr):
#             if a > 1:
#                 dp[a] += dp[a-1]
#             if a < len(arr):
#                 dp[a] += dp[a+1]
#             dp[a] += 1
#             if dp[a] == m:
#                 ans = idx+1
#             print(dp)

#         return ans
