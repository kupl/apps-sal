n = int(input())

hl = []
vl = []
z = []

for i in range(n**2):
    a, b = list(map(int, input().split()))
    if a in hl or b in vl:
        pass
    else:
        z.append(str(i + 1))
        hl.append(a)
        vl.append(b)
print(' '.join(z))
