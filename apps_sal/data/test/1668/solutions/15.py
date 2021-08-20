from collections import Counter
DIGS = '0123456789'
t = int(input())
for _ in range(t):
    n = int(input())
    P = [input() for _ in range(n)]
    print(sum((v - 1 for v in Counter(P).values())))
    for i in range(len(P)):
        if P[i] in P[:i]:
            for dig in DIGS:
                if dig + P[i][1:] not in P:
                    P[i] = dig + P[i][1:]
                    break
    for p in P:
        print(p)
