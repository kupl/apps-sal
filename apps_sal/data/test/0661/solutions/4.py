M, K = map(int, input().split())

if K >= pow(2, M):
    print(-1)
elif K == 0:
    ans = []
    for i in range(pow(2, M)):
        ans.append(i)
        ans.append(i)
    print(*ans)
else:
    num = 0
    L = []
    for i in range(pow(2, M)):
        if i == K:
            continue
        num ^= i
        L.append(i)
    if num == K:
        L2 = list(reversed(L))
        ans = L + [K] + L2 + [K]
        print(*ans)
    else:
        print(-1)
