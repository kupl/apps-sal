n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
f = [0] * n
gor = 0
for i in range(n):
    if i % 2 == 0 and i > 0:
        gor += c[i] - c[i - 1]
    elif i % 2 == 0:
        gor += c[i]
    f[i] = gor
if n % 2 == 0:
    gor += m - c[n - 1]


ma = gor

if c[0] > 1:
    if m - gor + 1 > ma:
        ma = m - gor + 1

for i in range(n):

    if i != n - 1:
        if c[i + 1] - c[i] > 1:
            if i % 2 == 0:
                t = (m - c[i] - 1) - (gor - f[i])

            else:
                t = (m - (c[i + 1] - 1)) - (gor - (f[i + 1] - 1))

            if t + f[i] > ma:
                ma = t + f[i]

    else:
        if m - c[i] > 1:
            if n % 2 == 1:
                t = gor + m - c[i] - 1
                if ma < t:
                    ma = gor + m - c[i] - 1

print(ma)
