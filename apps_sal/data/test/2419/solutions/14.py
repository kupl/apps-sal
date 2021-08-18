import bisect
import sys
input = sys.stdin.readline

t = int(input())

NLIST = [N * (N + 1) // 2 for N in range(10**5)]

for test in range(t):
    a, b = list(map(int, input().split()))

    x = abs(b - a)

    N = bisect.bisect_left(NLIST, x)

    while x % 2 != ((N + 1) // 2) % 2:
        N += 1

    print(N)
