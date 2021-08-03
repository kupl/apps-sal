n, z, w = map(int, input().split())

al = list(map(int, input().split()))

if n == 1:
    print(abs(al[0] - w))
    return

al1 = al[-2]
al2 = al[-1]

d1 = abs(al1 - al2)
d2 = abs(al2 - w)

print(max(d1, d2))
