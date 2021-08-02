import sys
input = sys.stdin.readline

t = int(input())

for testcases in range(t):
    a, b, c = list(map(int, input().split()))
    ANS = 0

    ANS += min(b, c // 2)
    b -= ANS
    ANS += min(a, b // 2)
    print(ANS * 3)
