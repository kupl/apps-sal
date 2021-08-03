N, M = map(int, input().split())
L = sorted(list(map(lambda x: (1, int(x)), input().split())) +
           [tuple(map(int, input().split())) for _ in range(M)]
           , key=lambda x: x[1], reverse=True)
ans, k = 0, 0
for n, a in L:
    if n + k >= N:
        ans += a * (N - k)
        break
    else:
        ans += a * n
        k += n
print(ans)
