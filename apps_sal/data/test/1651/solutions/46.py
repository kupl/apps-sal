S, P = map(int, input().split())
c = 0
routeP = int(P**0.5)
for N in range(1, routeP+1):
    if P % N == 0:
        M = int(P/N)
        if N + M == S:
            print('Yes')
            c += 1
            return
if c == 0:
    print('No')
