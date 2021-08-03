from sys import stdin

n, x, y = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
for i in range(n):
    t = True
    for j in range(i - 1, max(-1, i - x - 1), -1):
        if s[j] < s[i]:
            t = False
    for j in range(i + 1, min(n, i + y + 1)):
        if s[j] < s[i]:
            t = False
    if t:
        print(i + 1)
        break
