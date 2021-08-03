import sys
input = sys.stdin.readline

t = int(input())

for testcase in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = n - 1
    for i in range(n):
        if a[i] <= i - 1:
            left = i - 1
            break

    right = 0
    for i in range(n - 1, -1, -1):
        if a[i] < n - 1 - i:
            right = i + 1
            break

    if right <= left:
        print('Yes')
    else:
        print('No')
