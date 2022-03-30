def mapp(s):
    return 1 if s == '*' else 0


(n, m) = list(map(int, input().split()))
x = []
for i in range(n):
    x.append(list(map(mapp, input())))
s = [0] * m
for i in range(m):
    for j in range(n):
        s[i] += x[j][i]
h = 0
f = 0
for i in range(1, m):
    if s[i] - s[i - 1] > h:
        h = s[i] - s[i - 1]
    elif s[i] - s[i - 1] < f:
        f = s[i] - s[i - 1]
print(h, abs(f))
