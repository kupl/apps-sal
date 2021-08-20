(n, m) = map(int, input().split())
a = [int(x) % m for x in input().split()]
b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = (b[i] + a[i]) % m
key = dict()
key[0] = 0
for i in range(1, n + 1):
    if b[i] in key:
        key[b[i]] += 1
    else:
        key[b[i]] = 1
ans = key[0]
for value in key.values():
    ans += value * (value - 1) // 2
print(ans)
