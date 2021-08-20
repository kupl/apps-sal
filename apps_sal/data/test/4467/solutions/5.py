import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


'\nNが小さいので、Y座標でcandに入れておく\n'
N = ir()
AB = [lr() for _ in range(N)]
CD = [lr() for _ in range(N)]
cand = [0] * (2 * N)
ABCD = [(a, b, 0) for (a, b) in AB] + [(c, d, 1) for (c, d) in CD]
ABCD.sort()
answer = 0
for (X, Y, Z) in ABCD:
    if Z == 0:
        cand[Y] += 1
    else:
        for y in range(Y - 1, -1, -1):
            if cand[y] > 0:
                answer += 1
                cand[y] -= 1
                break
print(answer)
