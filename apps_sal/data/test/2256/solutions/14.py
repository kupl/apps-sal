import sys
input = sys.stdin.readline

t = int(input())

for testcases in range(t):
    n, x, a, b = list(map(int, input().split()))

    ANS = abs(b - a)

    print(min(n - 1, ANS + x))
