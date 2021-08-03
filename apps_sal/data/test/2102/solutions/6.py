a = list(map(int, input().split()))
n = int(input())
s = list(map(int, input().split()))
b = []
i = j = 0
ans = 10**18
cs = [0] * n
nz = 1
z = n * 6
for y in range(n):
    for x in a:
        b.append((s[y] - x) * n + y)
b.sort()
cs[b[0] % n] += 1
while j + 1 < z:
    while j + 1 < z and nz < n:
        j += 1
        nz += cs[b[j] % n] < 1
        cs[b[j] % n] += 1
    while nz == n:
        ans = min(ans, b[j] // n - b[i] // n)
        cs[b[i] % n] -= 1
        nz -= cs[b[i] % n] == 0
        i += 1
print(ans)
