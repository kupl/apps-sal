(n, m) = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
inter = a & b
if inter:
    print(min(inter))
else:
    mina = min(a)
    minb = min(b)
    if mina > minb:
        (mina, minb) = (minb, mina)
    print('{}{}'.format(mina, minb))
