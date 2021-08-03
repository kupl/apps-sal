n = int(input())
a = [int(s) for s in input().split()]

b = [0] * n
nb = 0

k = 0
while k < n and a[k] < 1:
    k += 1

if k > n - 1:
    print(0)
else:
    q = 1
    for i in range(k + 1, n):
        if a[i] == 1:
            nb += 1
            q += 1
        else:
            b[nb] += 1
    sum = 1
    for i in range(q - 1):
        sum *= (b[i] + 1)

    print(sum)
