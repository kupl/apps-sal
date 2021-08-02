n, k = list(map(int, input().split(' ')))
aaa = list(map(int, input().split(' ')))
ans = 0
v = []
for a in aaa:
    v.append((a * (a + 1)) / (2.0 * a))

current = 0
for i in range(n):
    current += v[i]
    if i >= k:
        current -= v[i - k]
    ans = max(ans, current)
print(ans)
