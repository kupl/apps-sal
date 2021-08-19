(N, M) = map(int, input().split())
A = [0] + list(map(int, input().split()))
a = 0
m = [0] * (N + 1)
for i in range(N + 1):
    a += A[i] % M
    a %= M
    m[i] = a
m.sort()
ans = 0
cnt = 1
for i in range(N):
    if m[i + 1] == m[i]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1
ans += cnt * (cnt - 1) // 2
print(ans)
