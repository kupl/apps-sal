import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    s = input()
    n = len(s) - 1
    ru = [0] * (n + 1)
    for i in range(n):
        if s[i] == "+":
            ru[i + 1] = ru[i] + 1
        else:
            ru[i + 1] = ru[i] - 1

    init = -1
    ans = 0
    for i, val in enumerate(ru):
        if val == init:
            ans += i
            init -= 1
    print(ans + n)
