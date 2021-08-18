from collections import defaultdict

N, M = list(map(int, input().split()))

G = defaultdict(list)

AB = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a, b
    G[a].append(b)
    G[b].append(a)
    AB.append((a, b))


def f(a, b):
    S = set([])
    Q = [1]
    while True:
        QQ = []
        for q in Q:
            S.add(q)
            for j in G[q]:
                if q == a and j == b:
                    continue
                if q == b and j == a:
                    continue
                if j not in S:
                    QQ.append(j)
        if len(QQ) == 0:
            break
        Q = QQ
    return 1 if len(S) != N else 0


cnt = 0
for a, b in AB:
    cnt += f(a, b)

print(cnt)
