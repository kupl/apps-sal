N = int(input())
M = 0
A = 0
R = 0
C = 0
H = 0
for i in range(N):
    S = input()
    s = S[0]
    if s == 'M':
        M += 1
    elif s == 'A':
        A += 1
    elif s == 'R':
        R += 1
    elif s == 'C':
        C += 1
    elif s == 'H':
        H += 1
ans = M * A * R + M * A * C + M * A * H + M * R * C + M * R * H + M * C * H + A * R * C + A * R * H + A * C * H + R * C * H
print(ans)
