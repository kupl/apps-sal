import sys
input = sys.stdin.readline
for _ in range(int(input())):
    r, g, b = list(map(int, input().split()))
    l = [r, g, b]
    l.sort()
    if l[2] > l[0] + l[1] + 1:
        print('No')
    else:
        print('Yes')
