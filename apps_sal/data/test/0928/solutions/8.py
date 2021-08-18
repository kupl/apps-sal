N, K = map(int, input().split())
a = list(map(int, input().split()))

s_a = 0
ans = 0
idx = 0
for i in range(N):

    while s_a < K:

        if(idx >= N):
            break

        s_a += a[idx]
        idx += 1
    if(s_a >= K):
        ans += N - idx + 1
        s_a -= a[i]
    else:
        break

print(ans)
