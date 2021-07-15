import sys
q = int(input())
for _ in range(q):
    k, n, a, b = map(int, sys.stdin.readline().split())
    if k-1-n*b < 0:
        print(-1)
        continue
    print(min(n, (k-1-n*b) // (a-b)))
