n, m = list(map(int, input().split()))
a = [int(input(), 2) for _ in range(n)]

l = a[::]
r = a[::]
f = 2**m - 1

for i in range(1, n):
    l[i] |= l[i - 1]
    r[-i - 1] |= r[-i]

res = False
for i in range(n):
    x = l[i - 1] if i != 0 else 0
    y = r[i + 1] if i != n - 1 else 0

    if (x | y) == f:
        res = True
        break

print("YES" if res else "NO")
