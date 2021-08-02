a = list(map(int, input().split()))
n = int(input())
s = list(map(int, input().split()))
b = []
for i in range(n):
    for j in a:
        b.append((s[i] - j) * n + i)
b = sorted(b)
cs = {}
i = j = 0
ans = 10**18
cs[b[0] % n] = cs.get(b[0] % n, 0) + 1
z = len(b)
while j < z:
    while j + 1 < z and len(cs) < n:
        j += 1
        cs[b[j] % n] = cs.get(b[j] % n, 0) + 1
    while len(cs) == n:
        ans = min(ans, b[j] // n - b[i] // n)
        cs[b[i] % n] -= 1
        if cs[b[i] % n] == 0:
            cs.pop(b[i] % n)
        i += 1
    if j + 1 == z:
        break
print(ans)
