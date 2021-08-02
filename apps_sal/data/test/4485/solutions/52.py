n, m, *AB = map(int, open(0).read().split())

C, D = set(), set()
for a, b in zip(AB[::2], AB[1::2]):
    if a == 1:
        C.add(b)
    if b == n:
        D.add(a)

if len(C & D):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
