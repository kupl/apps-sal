N, M, Q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for a in range(M):
    for b in range(a, M):
        for c in range(b, M):
            for d in range(c, M):
                for e in range(d, M):
                    for f in range(e, M):
                        for g in range(f, M):
                            for h in range(g, M):
                                for i in range(h, M):
                                    for j in range(i, M):
                                        tmp = [a, b, c, d, e, f, g, h, i, j]
                                        tmp_ans = 0
                                        for q in range(Q):
                                            if tmp[L[q][1] - 1] - tmp[L[q][0] - 1] == L[q][2]:
                                                tmp_ans += L[q][3]

                                        ans = max(ans, tmp_ans)

print(ans)
