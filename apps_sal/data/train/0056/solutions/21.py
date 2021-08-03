import sys
input = sys.stdin.readline
def inputr(): return sys.stdin.readline().rstrip('\n')


for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    e = k // n
    T = [[0] * n for _ in range(n)]

    for i in range((k + n - 1) // n):
        for j in range(min(n, k - i * n)):
            T[j][(i + j) % n] = 1

    rows = [sum(R) for R in T]
    cols = [sum(C) for C in zip(*T)]
    assert sum(rows) == k
    assert sum(cols) == k
    print((max(rows) - min(rows)) ** 2 + (max(cols) - min(cols)) ** 2)
    for R in T:
        print(''.join(map(str, R)))
