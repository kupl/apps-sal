(n, h, *L) = map(int, open((x := 0)).read().split())
a = max(L[::2])
B = sorted([l for l in L[1::2] if l > a])
for b in B[::-1]:
    h -= b
    x += 1
    if h < 1:
        break
print(x - min(0, -h // a))
