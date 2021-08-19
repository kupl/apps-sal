n = int(input())
a = [int(c) for c in input()]
while a and a[-1] == 0:
    a.pop()
n = len(a)
acc = [0] * (n + 1)
for i in range(1, n + 1):
    acc[i] = acc[i - 1] + a[i - 1]
res = n == 0
for l in range(1, n):
    pos = l
    res2 = True
    while pos < n and res2:
        for i in range(pos + 1, n + 1):
            if acc[i] - acc[pos] == acc[l]:
                pos = i
                break
            if acc[i] - acc[pos] > acc[l] or i == n:
                res2 = False
                break
    if res2:
        res = True
        break
print('YES' if res else 'NO')
