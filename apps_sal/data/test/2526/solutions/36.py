from sys import stdin
nii = lambda: map(int, stdin.readline().split())
lnii = lambda: list(map(int, stdin.readline().split()))

x, y, a, b, c = nii()
p = lnii()
q = lnii()
r = lnii()

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

l = p[:x] + q[:y]
l.sort()

ans = 0
for i in range(x + y):
    if i < c:
        ans += max(l[i], r[i])
    else:
        ans += l[i]

print(ans)
