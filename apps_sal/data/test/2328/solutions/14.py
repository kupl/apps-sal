import sys
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()


for _ in range(q):
    n, k = mi()

    l = lm()

    m = float('Inf')

    for i in range(0, n - k):

        if l[i + k] - l[i] < m:
            m = l[i + k] - l[i]
            x = (l[i + k] + l[i]) // 2

    print(x)
