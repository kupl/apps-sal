n, a = map(int, input().split())
t = list(map(int, input().split()))
a -= 1
d = [0] * n
for i in range(n):
    if t[i] == 1:
        d[abs(i - a)] += 1

res = 0
i1 = i2 = a
for i in range(n):
    if d[i] == 2:
        res += 2
    elif d[i] == 1 and (i1 < 0 or i2 >= n or i1 == i2):
        res += 1
    i1 -= 1
    i2 += 1
print(res)
