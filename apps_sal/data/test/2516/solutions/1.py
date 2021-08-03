n, p = map(int, input().split())
s = input()
a = []
c = 0
if p == 2:
    b = [0] * n
    for i in range(n):
        if int(s[i]) % 2 == 0:
            b[i] += 1
    for i in range(n):
        if b[i] == 1:
            c += i + 1
elif p == 5:
    b = [0] * n
    for i in range(n):
        if int(s[i]) % 5 == 0:
            b[i] += 1
    for i in range(n):
        if b[i] == 1:
            c += i + 1
else:
    b = [0] * p
    b[0] = 1
    d = [1]
    a.append(int(s[-1]) % p)
    for i in range(n - 1):
        d.append(d[-1] * 10 % p)
    for i in range(1, n):
        a.append((int(s[-i - 1]) * d[i] + a[i - 1]) % p)
    for i in range(n):
        b[a[i]] += 1
    for i in range(p):
        c += int(b[i] * (b[i] - 1) / 2)
print(c)
