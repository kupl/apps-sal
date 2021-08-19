import sys
input = sys.stdin.readline
t = int(input())
for testcases in range(t):
    n = int(input())
    S = input().strip()
    ANS = n
    if '1' in S:
        t = S.index('1')
        ANS = max(ANS, (n - t) * 2)
        t = S[::-1].index('1')
        ANS = max(ANS, (n - t) * 2)
    print(ANS)
