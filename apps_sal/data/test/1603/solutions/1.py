n = int(input().strip())
v = list(map(int, input().split()))
m = int(input().strip())
f1 = [0] * n
f2 = [0] * n
u = sorted(v)
for i in range(n):
    f1[i] = v[i]
    if i > 0:
        f1[i] += f1[i - 1]

for i in range(n):
    f2[i] = u[i]
    if i > 0:
        f2[i] += f2[i - 1]

ans = []

for i in range(m):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if t == 1:
        an = f1[r]
        if l > 0:
            an -= f1[l - 1]
        ans.append(an)
    else:
        an = f2[r]
        if l > 0:
            an -= f2[l - 1]
        ans.append(an)

print(*ans, sep='\n')
