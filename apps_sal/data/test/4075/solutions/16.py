def func(sw, p, bit):
    sum_on = 0
    for k in range(sw[0]):
        idx = sw[k + 1] - 1
        if bit[idx] == 1:
            sum_on += 1
    if sum_on % 2 == p:
        res = 1
    else:
        res = 0
    return res


(N, M) = list(map(int, input().split()))
SW = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))
ans = 0
for i in range(1 << N):
    bit = [0] * N
    for j in range(N):
        div = 1 << j
        bit[j] = i // div % 2
    cnt = 0
    for m in range(M):
        res = func(SW[m], P[m], bit)
        if res == 1:
            cnt += 1
    if cnt == M:
        ans += 1
print(ans)
