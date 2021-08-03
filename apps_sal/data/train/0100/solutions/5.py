import sys
input = sys.stdin.readline

t = int(input())
for testcases in range(t):
    r, g, b = sorted(map(int, input().split()))

    if b > r + g:
        print(r + g)
    else:
        print((r + g + b) // 2)
