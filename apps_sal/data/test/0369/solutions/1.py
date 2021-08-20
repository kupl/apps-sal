(N, M) = map(int, input().split())
S = list(map(int, reversed(input())))
now = 0
ans = []
while now + M < N:
    last = now
    now += M
    while S[now]:
        now -= 1
    if last == now:
        print(-1)
        break
    ans.append(now - last)
else:
    print(*reversed(ans + [N - now]))
