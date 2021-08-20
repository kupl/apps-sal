from bisect import bisect_left
n = int(input())
mas = []
for i in range(n):
    mas.append(0)
for i in range(n):
    (x, y) = list(map(int, input().split()))
    mas[x] = max(mas[x], y)
w = list(map(int, input().split()))
for i in range(n):
    w[i] = -w[i]
s = []
r = []
res1 = []
res2 = []
res3 = []
for i in range(n):
    s.append(i)
    r.append(i)
    res2.append(-1)
    s[i] -= mas[i] + 1
error = 0
for i in range(n):
    if error == 1:
        break
    t = bisect_left(r, w[i])
    if t >= n or r[t] != w[i]:
        error = 1
        break
    else:
        r[t] = r[t] - 1
        if r[t] < s[t] or (t > 0 and r[t] == r[t - 1]):
            error = 1
            break
    res1.append(t)
    res2[t] = res2[t] + 1
    res3.append(res2[t])
if error == 1:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(str(res1[i]) + ' ' + str(res3[i]))
