def cnt(s, x): return s.count(x)
def ii(): return int(input())
def si(): return input()
def f(): return list(map(int, input().split()))
def dgl(): return list(map(int, input()))
def il(): return list(map(int, input().split()))


n, k = f()
l = [0] * (n + 10)
p = []
mx = 0
for _ in range(k):
    a, b = f()
    p.append([a, b])
    l[a] += 1
    l[b + 1] -= 1

psf = [l[0]]

for _ in range(1, n + 2):
    psf.append(psf[-1] + l[_])

w = sum(i > 0 for i in psf)

psf1, psf2 = [0], [0]
for i in range(1, n + 2):
    if psf[i] == 1:
        psf1.append(psf1[-1] + 1)
    else:
        psf1.append(psf1[-1])
    if psf[i] == 2:
        psf2.append(psf2[-1] + 1)
    else:
        psf2.append(psf2[-1])


for i in range(k - 1):
    for j in range(i + 1, k):
        x = w - (psf1[p[i][1]] - psf1[p[i][0] - 1]) - (psf1[p[j][1]] - psf1[p[j][0] - 1])
        l, r = max(p[i][0], p[j][0]), min(p[i][1], p[j][1])
        if l <= r:
            x += psf1[r] - psf1[l - 1]
            x -= psf2[r] - psf2[l - 1]
        mx = max(x, mx)


print(mx)
