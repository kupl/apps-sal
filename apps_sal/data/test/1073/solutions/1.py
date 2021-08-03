k = 0

a = int(input())
b = input()
u = [0] * 205
r = [0] * 205
l = [0] * 205
d = [0] * 205

for i in range(a):
    u[i + 1] = u[i]
    r[i + 1] = r[i]
    d[i + 1] = d[i]
    l[i + 1] = l[i]
    if (b[i] == 'U'):
        u[i + 1] += 1
    elif b[i] == 'R':
        r[i + 1] += 1
    elif b[i] == 'L':
        l[i + 1] += 1
    else:
        d[i + 1] += 1

for i in range(1, a + 1):
    for j in range(i, a + 1):
        if u[j] - u[i - 1] == d[j] - d[i - 1] and l[j] - l[i - 1] == r[j] - r[i - 1]:
            k += 1

print(k)
