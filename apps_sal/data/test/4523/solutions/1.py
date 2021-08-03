import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = "YES"
    for i in range(1, n):
        if a[i] - a[i - 1] >= 2:
            flag = "NO"
            break
    print(flag)
