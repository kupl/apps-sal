import sys
input = sys.stdin.readline
t = int(input())
while t:
    t -= 1
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) >= m:
        print(m)
    else:
        print(sum(a))
