n, m, c = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(m)]) + c > 0:
        ans += 1
print(ans)
