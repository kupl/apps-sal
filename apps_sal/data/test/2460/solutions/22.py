(n, m) = list(map(int, input().split()))
x = input().split()
t = input().split()
r = [0] * n
d = [0] * m
countr = 0
countd = 0
for i in range(n + m):
    if int(t[i]) == 1:
        d[countd] = int(x[i])
        countd += 1
    else:
        r[countr] = int(x[i])
        countr += 1
current = 0
count = [0] * m
for i in range(n):
    while current < m - 1:
        if d[current + 1] >= r[i]:
            break
        current += 1
    if current == m - 1:
        count[m - 1] += n - i
        break
    if 2 * r[i] <= d[current] + d[current + 1]:
        count[current] += 1
    else:
        count[current + 1] += 1
s = ''
for i in range(m):
    s += str(count[i]) + ' '
print(s[:-1])
