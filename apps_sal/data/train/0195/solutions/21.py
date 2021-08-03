class Solution:
    def countTriplets(self, A: List[int]) -> int:

        B = [bin(a)[2:] for a in A]
        M, N = len(B), max(list(map(len, B)))
        B = [b.zfill(N) for b in B]

        dic = collections.defaultdict(set)
        for i in range(M):
            for j in range(N):
                if B[i][j] == '1':
                    dic[j].add(i)

        Venn = collections.defaultdict(list)
        cnt = 0
        for j in range(N):
            if len(dic[j]):
                cnt += (len(dic[j])) ** 3
                for i in range(j, 0, -1):
                    for prv in Venn[i]:
                        intersec = prv & dic[j]
                        if len(intersec):
                            cnt += ((-1) ** i) * (len(intersec)) ** 3
                            Venn[i + 1].append(intersec)
                Venn[1].append(dic[j])

        return M ** 3 - cnt


#         # ans = 0
#         n = len(A)

#         @lru_cache(None)
#         def dfs(i, pre):
#             if i == 4 and not pre:
#                 return 1
#             ans = 0
#             for a in A:
#                 if (i > 1 and not pre & a) or (i == 1 and not a):
#                     ans += n ** (3 - i)
#                 elif i < 3:
#                     ans += dfs(i + 1, pre & a if i > 1 else a)
#             return ans


#         return dfs(1, None)
