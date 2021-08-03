import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for x in range(1, 1024):
        b = [0] * N
        for i in range(N):
            b[i] = a[i] ^ x
        b.sort()
        if a == b:
            print(x)
            break
    else:
        print(-1)
