import sys
# q=2
q = int(input())
for i in range(q):
    n, m = [int(j) for j in sys.stdin.readline().split()]
    # n=int(sys.stdin.readline())
    #a=[int(j) for j in sys.stdin.readline().split()]
    # a=sys.stdin.readline().strip()
    if n * 2 > m:
        print(-1, -1)
    else:
        print(n, n * 2)
