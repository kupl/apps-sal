(N, M) = list(map(int, input().split()))
s_lst = [[False] * N for _ in range(M)]
for i in range(M):
    ks = list(map(int, input().split()))
    for (j, value) in enumerate(ks):
        if j != 0:
            s_lst[i][value - 1] = True
p = list(map(int, input().split()))
ans = 0
for bit in range(2 ** N):
    cnt = [0] * M
    for i in range(N):
        if bit >> i & 1 == 1:
            for j in range(M):
                if s_lst[j][i]:
                    cnt[j] += 1
    flug = True
    for i in range(M):
        if cnt[i] % 2 != p[i]:
            flug = False
    if flug:
        ans += 1
print(ans)
