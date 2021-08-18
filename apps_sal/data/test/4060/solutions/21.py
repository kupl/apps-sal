n = int(input())
s = input()
a = []
for i in s:
    if i == '(':
        a.append(-1)
    else:
        a.append(1)
b = [0] * (n)
b[0] = a[0]
for i in range(1, n):
    b[i] = a[i] + b[i - 1]
e = []
c = d = 0
for i in range(n - 1, -1, -1):
    if b[i] >= -1:
        c += 1
    if b[i] >= 3:
        d += 1
    e.append((c, d))
e = e[::-1]
g = 0
ans = 0
for i in range(n):
    if a[i] == -1:
        if e[i][0] == 0 and (b[-1] + 2) == 0 and g == 0:
            ans += 1
    else:
        if e[i][1] == 0 and (b[-1] - 2) == 0 and g == 0:
            ans += 1
    if b[i] > 0:
        g += 1
print(ans)
