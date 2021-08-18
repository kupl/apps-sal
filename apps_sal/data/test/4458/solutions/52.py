N = int(input())
p = list(map(int, input().split()))


m = [0] * (N)
m[0] = p[0]
for i in range(1, N):
    m[i] = min(m[i - 1], p[i])

ans = 1
for i in range(1, N):
    if m[i - 1] >= p[i]:
        ans += 1

print(ans)
