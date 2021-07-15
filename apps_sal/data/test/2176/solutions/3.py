from sys import stdin
input = stdin.readline
n = int(input())
p = 998244353
sil = [0] * 400000
sil[1] = 1
for i in range(2, 400000):
    sil[i] = (sil[i -1] * i) % p
def fun(l):
    wyn = 1
    l.sort()
    count = 1
    for i in range(1, len(l)):
        if l[i] != l[i-1]:
            wyn = (wyn * sil[count]) % p
            count = 1
        else:
            count += 1
    wyn = (wyn * sil[count]) % p
    return wyn
dupa = [list(map(int,input().split())) for i in range(n)]
xx = [i[0] for i in dupa]
yy = [i[1] for i in dupa]
dupa.sort()
x = [i[0] for i in dupa]
y = [i[1] for i in dupa]
dolne = []
pyk = 1
left = 0
for i in range(1, n):
    if x[i] != x[i-1]:
        dolne.append(y[left:i])
        left = i
if left == n - 1:
    dolne.append([y[n - 1]])
else:
    dolne.append(y[left:n])
c = 1
for i in range(1, len(dolne)):
    if min(dolne[i]) < max(dolne[i - 1]):
        c = 0
        break
# c = 0 means no overlaps

wyn = fun(xx) + fun(yy)
if c == 1:
    dupa = 1
    for i in range(len(dolne)):
        dupa = (dupa * fun(dolne[i])) % p
    wyn -= dupa
print((sil[n] - wyn) % p)
