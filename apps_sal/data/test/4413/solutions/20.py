import sys
input = sys.stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            print(2)
            break
    else:
        print(1)
