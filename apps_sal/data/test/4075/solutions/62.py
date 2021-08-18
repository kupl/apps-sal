N, M = map(int, input().split())
ks = [list(map(int, input().split()))[1:] for _ in range(M)]
P = list(map(int, input().split()))
temp = [0] * M

ans = 0

for i in range(2**N):
    temp = [0] * M
    for h in range(N):
        if i >> h & 1:
            for g in range(M):
                if h + 1 in ks[g]:
                    temp[g] += 1
    for k in range(M):
        temp[k] = temp[k] % 2
    if temp == P:
        ans += 1


print(ans)
