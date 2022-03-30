(n, m) = map(int, input().split())
A = [0] * n
for i in range(n):
    per = input()
    A[i] = per
t = n
for i in range(n):
    if A[i][0] == '*':
        t = i
        break
per1 = 0
per2 = 0
for j in range(1, m):
    s = m
    for i in range(n):
        if A[i][j] == '*':
            s = i
            break
    if t > s:
        per1 = max(per1, t - s)
    else:
        per2 = max(per2, s - t)
    t = s
print(per1, per2)
