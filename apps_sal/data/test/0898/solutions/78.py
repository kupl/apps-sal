(n, m) = map(int, input().split())
ans = 1
for i in range(1, int(m ** 0.5) + 1):
    if m % i:
        continue
    if m // i >= n and i > ans:
        ans = i
    if i >= n and m // i >= ans:
        ans = m // i
print(ans)
