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
