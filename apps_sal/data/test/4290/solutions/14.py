import itertools
n, m = list(map(int, input().split()))
ln = []
ans = 0
for i in range(n):
    ln.append(2)
for i in range(m):
    ln.append(3)
for x in itertools.combinations(ln, 2):
    if (x[0]+x[1]) % 2 == 0:
        ans += 1
print(ans)

