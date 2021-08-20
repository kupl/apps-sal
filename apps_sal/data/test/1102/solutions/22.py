[n, a] = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))
m1 = min(n - a, a - 1)
s = t[a - 1]
for i in range(1, m1 + 1):
    if t[a - 1 - i] + t[a - 1 + i] == 2:
        s += 2
for i in range(n):
    if abs(a - 1 - i) <= m1:
        continue
    s += t[i]
print(s)
