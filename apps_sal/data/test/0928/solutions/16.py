(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [0] * (N + 1)
for i in range(1, N + 1):
    b[i] = b[i - 1] + a[i - 1]
ans = 0
j = 0
for i in range(1, N + 1):
    if b[i] - b[j] < K:
        continue
    ans += N + 1 - i
    while i > j:
        j += 1
        if b[i] - b[j] >= K:
            ans += N + 1 - i
        else:
            break
print(ans)
