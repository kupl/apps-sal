(n, m) = map(int, input().split())
ok = [0] * (n + 2)
ans = 0
for _ in range(m):
    (l, r) = map(int, input().split())
    ok[l] += 1
    ok[r + 1] -= 1
for i in range(1, n + 2):
    ok[i] += ok[i - 1]
    if ok[i] == m:
        ans += 1
print(ans)
