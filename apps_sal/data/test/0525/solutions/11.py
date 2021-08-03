import sys
input = sys.stdin.readline
for f in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    iseq = True
    for i in range(1, n):
        if a[i] != a[i - 1]:
            iseq = False
    if iseq:
        print(n)
    else:
        print(1)
