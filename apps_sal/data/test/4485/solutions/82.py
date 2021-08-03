N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]

s1 = set()
sn = set()
for a, b in AB:
    if a == 1:
        s1.add(b)
    if b == N:
        sn.add(a)

print('POSSIBLE' if s1 & sn else 'IMPOSSIBLE')
