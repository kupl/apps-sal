N = int(input())
P = list(map(int, input().split()))

indexes = [x for x in range(N + 1)]
for i in range(N):
    indexes[P[i]] = i

moves = {}
for i in range(1, N):
    moves[i] = False

conf = []
for i in range(1, N + 1):
    while indexes[i] != i - 1:
        if moves[indexes[i]] is True:
            print((-1))
            return
        conf.append(indexes[i])
        moves[indexes[i]] = True

        a, b = P[indexes[i] - 1], P[indexes[i]]
        P[indexes[i] - 1], P[indexes[i]] = b, a
        indexes[b], indexes[a] = indexes[a], indexes[b]

if not all(moves.values()):
    print((-1))
else:
    print(("\n".join(map(str, conf))))
