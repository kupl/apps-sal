n = int(input())
a = [int(x) for x in input().strip().split()]

f = dict()
b = dict()
for i in range(len(a)):
    if a[i] not in f:
        f[a[i]] = i
    if a[n-1-i] not in b:
        b[a[n-1-i]] = n-1-i

f = sorted([v, k] for k, v in list(f.items()))
b = sorted([v, k] for k, v in list(b.items()))

ans = 0
bi = 0
for i, v in f:
    while bi < len(b) and i >= b[bi][0]:
        bi += 1
    ans += len(b) - bi

print(ans)

