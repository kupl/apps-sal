(N, K) = map(int, input().split())
c = N
ans = 1
if K == 1:
    print(0)
else:
    while c < K:
        ans += 1
        c += N - 1
    print(ans)
