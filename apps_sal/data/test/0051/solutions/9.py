a = input()
n = len(a)
z = list(0 for mas in range(n))
z[0] = n
L = R = 0
for i in range(1, n):
    if i <= R:
        if z[i - L] < R - i + 1:
            z[i] = z[i - L]
        else:
            j = 1
            while (R + j < n) and (a[R + j] == a[R - i + j]):
                j += 1
            z[i] = R - i + j
            L = i
            R += j - 1
    else:
        j = 0
        while (i + j < n) and (a[i + j] == a[j]):
            j += 1
        z[i] = j
        L = i
        R = i + j - 1
q = n // 2
if (n % 2 == 0):
    q -= 1
u = -1
for i in range(1, q + 1):
    if z[i] + i == n:
        u = i
if u == -1:
    print('NO')
else:
    print('YES')
    print(a[u::])
