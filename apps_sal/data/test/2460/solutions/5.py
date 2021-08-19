(n, m) = map(int, input().split())
xi = list(map(int, input().split()))
ti = list(map(int, input().split()))
ai = [0] * (m + 2)
ar = [0] * (m + 2)
ar[-1] = 10 ** 11
ar[0] = -100000000000
j = 1
n2 = n + m
for i in range(n2):
    if ti[i] == 1:
        ar[j] = xi[i]
        j += 1
i1 = 0
i2 = 1
for i in range(n2):
    if ti[i] == 1:
        i2 += 1
        i1 += 1
        continue
    num = xi[i] - ar[i1]
    num2 = ar[i2] - xi[i]
    if num <= num2:
        ai[i1] += 1
    else:
        ai[i2] += 1
for i in range(1, m + 1):
    print(ai[i], end=' ')
