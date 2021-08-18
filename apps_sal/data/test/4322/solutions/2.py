def rint(): return int(input())
def rmint(): return map(int, input().split())
def rlist(): return list(rmint())


n = rint()
a = [0, 0] * (10 ** 5 + 1)
for c in rlist():
    a[c] += 1
pr = 0
t = 0
ans = 0
g = 0
for i in range(1, 2 * 10 ** 5 + 1):
    if a[i] < 2:
        t = 0
        pr = a[i]
    else:
        t += a[i]
    nx = a[i + 1]
    if pr + t + nx > ans:
        ans = pr + t + nx
        g = i
r = g + 1
l = g + 1
while a[l - 1] > 1:
    l -= 1
while a[r] > 1:
    r += 1
print(ans)


def out(x, y=1):
    while y:
        print(x, end=' ')
        y -= 1


for i in range(l, r):
    out(i)
out(r, a[r])
for i in range(r - 1, l - 1, -1):
    out(i, a[i] - 1)
out(l - 1, a[l - 1])
