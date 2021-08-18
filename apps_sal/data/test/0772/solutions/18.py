a, b, c = list(map(int, input().split()))
e, f, g = list(map(int, input().split()))
m, n, l = list(map(int, input().split()))
p = 1
q = 1
r = 1
s = 1
t = 1
u = 1
v = 1
w = 1
x = 1
k = [p, q, r, s, t, u, v, w, x]
j = [a, b, c, e, f, g, m, n, l]


def change(l, h):
    kas = l[h]
    if kas == 1:
        l[h] = 0
    if kas == 0:
        l[h] = 1


for d in range(3):
    if j[d] % 2 != 0 and j[d] != 0:
        change(k, d)
        if d != 2:
            change(k, d + 1)
        if d != 0:
            change(k, d - 1)
        change(k, d + 3)

for d in range(3, 6):
    if j[d] % 2 != 0 and j[d] != 0:
        change(k, d)
        if d != 5:
            change(k, d + 1)

        if d != 3:
            change(k, d - 1)
        change(k, d + 3)
        change(k, d - 3)

for d in range(6, 9):
    if j[d] % 2 != 0 and j[d] != 0:
        change(k, d)
        if d != 8:
            change(k, d + 1)
        if d != 6:
            change(k, d - 1)
        change(k, d - 3)
S0 = str(k[0])
S1 = str(k[1])
S2 = str(k[2])
S3 = str(k[3])
S4 = str(k[4])
S6 = str(k[6])
S5 = str(k[5])
S7 = str(k[7])
S8 = str(k[8])

print(S0 + S1 + S2)
print(S3 + S4 + S5)
print(S6 + S7 + S8)
