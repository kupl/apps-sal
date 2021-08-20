import sys
input = sys.stdin.readline


def calc(A):
    M = max(A)
    return [M - a for a in A]


t = int(input())
for tests in range(t):
    (n, k) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if k % 2 == 0:
        k = 2
    else:
        k = 1
    for j in range(k):
        A = calc(A)
    print(*A)
