import sys


def input():
    return sys.stdin.readline().rstrip()


def calc(n, k, A):
    X = [[0] * 26 for _ in range((k + 1) // 2)]
    for (i, a) in enumerate(A):
        j = i % k
        j = min(j, k - 1 - j)
        X[j][a] += 1
    return sum([sum(x) - max(x) for x in X])


T = int(input())
for _ in range(T):
    (N, K) = list(map(int, input().split()))
    S = [ord(a) - 97 for a in input()]
    print(calc(N, K, S))
