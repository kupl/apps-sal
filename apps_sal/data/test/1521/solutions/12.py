p, n = map(int, input().split())
x = []
for i in range(n):
    x.append(int(input()))
pos = []
out = -1
for i in range(n):
    a = x[i] % p
    if a in pos:
        out = (i + 1)
        break
    else:
        pos.append(a)

if out == -1:
    print(-1)
else:
    print(out)
