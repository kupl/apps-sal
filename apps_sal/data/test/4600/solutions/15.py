N, M = map(int, input().split())
ac = set()
pena = 0
walen = [0] * N

for i in range(M):
    p, S = map(str, input().split())
    p = int(p) - 1
    if p in ac:
        continue
    elif S == 'AC':
        ac.add(p)
        pena += walen[p]
    else:
        walen[p] += 1

print(len(ac), pena)
