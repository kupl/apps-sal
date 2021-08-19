(N, K) = map(int, input().split())
a = [i for i in range(1, N + 1)]
ans = 0
for b in range(1, N + 1):
    if K >= b:
        continue
    elif K != 0:
        ans += N // b * (b - K) + max(N % b - K + 1, 0)
    else:
        ans += N
print(ans)
