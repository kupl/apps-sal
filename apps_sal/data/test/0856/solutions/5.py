import sys
input = sys.stdin.readline
t = int(input())
while t:
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    mx = max(l)
    for i in range(n):
        l[i] = mx - l[i]
    k -= 1
    if k % 2 == 0:
        print(*l)
    else:
        mx = max(l)
        for i in range(n):
            l[i] = mx - l[i]
        print(*l)
    t -= 1
