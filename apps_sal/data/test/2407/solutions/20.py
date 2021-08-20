import sys
input = sys.stdin.readline
for i in range(int(input())):
    (n, r) = list(map(int, input().split()))
    a = sorted(list(set(list(map(int, input().split())))), reverse=True)
    i = 0
    se = 0
    n = len(a)
    while i < n and a[i] - se > 0:
        i += 1
        se += r
    print(i)
