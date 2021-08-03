n, m = map(int, input().split())
P = [0] * n
AC = 0
WA = 0
for i in range(m):
    p, S = input().split()
    p = int(p)
    if S == "AC" and P[p - 1] != -1:
        WA += P[p - 1]
        AC += 1
        P[p - 1] = -1
    elif S == "WA" and P[p - 1] != -1:
        P[p - 1] += 1
print(AC, WA)
