n = int(input())
l = [int(input()) for _ in range(n)]

i = 0
n2 = 1 << n
res = False
while i < n2:
    b = bin(i)[2:].zfill(n)
    s = 0
    for j, e in enumerate(b):
        if e == '0':
            s += l[j]
        else:
            s -= l[j]
    if s % 360 == 0:
        res = True
    i += 1

if res:
    print("YES")
else:
    print("NO")
