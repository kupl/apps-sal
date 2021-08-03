n = int(input())
i = 0
s = 0
t = 0
x = 0
f = 0
res1 = []
res2 = []
while n >= 0:
    i = i + 1
    n = n - i * i
    if (n < 0):
        break
    t = t + i
    m = n // t
    if (m * t != n):
        continue
    else:
        res1.append(i)
        res2.append(m + i)
        x = x + 1
        if m == 0:
            f = 1

print(str(int(2 * x - f)))
for i in range(x):
    print(str(int(res1[i])) + " " + str(int(res2[i])))
res1.reverse()
res2.reverse()
for i in range(x):
    if (res1[i] != res2[i]):
        print(str(int(res2[i])) + " " + str(int(res1[i])))
