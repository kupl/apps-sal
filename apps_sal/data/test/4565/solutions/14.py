n = int(input())
s = input()
w = [0] * n
e = [0] * n
if s[0] == 'W':
    w[0] = 1
else:
    e[0] = 1
for i in range(1, n):
    if s[i] == 'W':
        w[i] = w[i - 1] + 1
        e[i] = e[i - 1]
    else:
        w[i] = w[i - 1]
        e[i] = e[i - 1] + 1
ans = float('inf')
for i in range(n):
    t = 0
    if i != 0:
        t += w[i - 1]
    if i != n - 1:
        t += e[-1] - e[i]
    if t < ans:
        ans = t
print(ans)
