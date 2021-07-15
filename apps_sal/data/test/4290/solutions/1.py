n, m = list(map(int, input().split()))
ln = []
ans = 0
for i in range(n):
    ln.append(2)
for i in range(m):
    ln.append(3)
for a in range(len(ln)):
    for b in range(len(ln)):
        if a != b:
            if (ln[a]+ln[b]) % 2 == 0:
                ans += 1
print((ans//2))

