import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    for i in range(n - 1):
        if L[i + 1] - L[i] > 1:
            print('NO')
            break
    else:
        print('YES')
