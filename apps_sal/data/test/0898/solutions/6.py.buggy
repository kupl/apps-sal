import math
N, M = list(map(int, input().split()))

G = []
for i in range(1, int(math.sqrt(M)) + 2 + 1):
    if M % i == 0:
        cd = M // i
        G.append(cd)
        G.append(i)

G.sort(reverse=True)
for g in G:
    n = M // g
    if n >= N:
        print(g)
        return
