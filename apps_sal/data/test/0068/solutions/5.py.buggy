import sys

n = int(input())
S = input()
x, y = list(map(int, input().split()))

if abs(x) + abs(y) > n or (abs(x) + abs(y)) % 2 != n % 2:
    print(-1)
    return

now = [0, 0]
LISTL = [(0, 0)]
for s in S:
    if s == "R":
        now[0] += 1
    elif s == "L":
        now[0] -= 1
    elif s == "U":
        now[1] += 1
    else:
        now[1] -= 1

    LISTL.append((now[0], now[1]))

LISTR = [(0, 0)]
now = [0, 0]
for s in S[::-1]:
    if s == "R":
        now[0] += 1
    elif s == "L":
        now[0] -= 1
    elif s == "U":
        now[1] += 1
    else:
        now[1] -= 1

    LISTR.append((now[0], now[1]))


def su(a, b, x, y):
    return abs(x - (a[0] + b[0])) + abs(y - (a[1] + b[1]))


ANS = 0
for i in range(n + 1):
    for j in range(max(0, ANS - i), n + 1):
        if su(LISTR[i], LISTL[j], x, y) <= n - i - j:
            # print(i,j)
            if ANS < i + j:
                ANS = i + j

        else:
            break

print(n - ANS)
