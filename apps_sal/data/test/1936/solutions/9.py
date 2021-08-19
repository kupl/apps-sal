import sys
q = int(input())
for i in range(q):
    (n, m) = [int(j) for j in sys.stdin.readline().split()]
    if n * 2 > m:
        print(-1, -1)
    else:
        print(n, n * 2)
