from collections import Counter
N = int(input())
C = list(Counter(map(int, input().split())).values())
C.sort()

rest = N
removed = 0
for K in range(1, N + 1):
    d = K - removed
    while C and C[- 1] > rest // d:
        rest -= C[- 1]
        C.pop()
        removed += 1
        d -= 1
    print(rest // d)
