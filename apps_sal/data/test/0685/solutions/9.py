
n, h = map(int, input().split())
s = [0 for i in range(n)]
e = [0 for i in range(n)]

for i in range(n):
    s[i], e[i] = map(int, input().split())

L = 0
R = 0
H = h
M = 0

while L < n:
    while (R < n - 1) and (H - (s[R + 1] - e[R]) > 0):
        H -= (s[R + 1] - e[R])
        R += 1

    if e[R] - s[L] + H > M:
        M = e[R] - s[L] + H

    if L < n - 1:
        H += s[L + 1] - e[L]

    L += 1

print(M)
