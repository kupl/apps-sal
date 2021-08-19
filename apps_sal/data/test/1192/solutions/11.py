from random import randint
(n, k) = list(map(int, input().split()))
perm = list(map(int, input().split()))
moves = []
for i in range(n):
    for j in range(i, n):
        moves.append((i, j))


def go(p, cnt):
    if cnt == k:
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if p[j] < p[i]:
                    ret += 1
        return ret
    ans = 0
    for move in moves:
        (fr, to) = move
        nx = p[fr:to + 1]
        ans += go(p[:fr] + nx[::-1] + p[to + 1:], cnt + 1)
    return ans


print(go(perm, 0) / pow(len(moves) * 1.0, k))
