import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 9)


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nn():
    return list(stdin.readline().split())


def ns():
    return stdin.readline().rstrip()


n = ns()
n = list(map(int, n[::-1])) + [0]
ans = 0
for i in range(len(n)):
    a = n[i]
    if a <= 4:
        ans += a
    elif a >= 6:
        ans += 10 - a
        n[i + 1] += 1
    elif n[i + 1] <= 4:
        ans += a
    else:
        ans += a
        n[i + 1] += 1
print(ans)
