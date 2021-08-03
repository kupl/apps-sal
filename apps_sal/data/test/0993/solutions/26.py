n, m = map(int, input().split())
a = list(map(int, input().split()))
table = {0: 0}
s = a[0] % m
table[s] = 1
for i in range(1, n):
    s = (s + a[i]) % m
    if s in table:
        table[s] += 1
    else:
        table[s] = 1
ans = 0
for i in table.values():
    ans += (i * (i - 1)) // 2
print(ans + table[0])
