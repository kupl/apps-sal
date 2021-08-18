n, m = [int(i) for i in input().split()]
a = [(n - i) // m + 1 for i in range(0, m + 1)]
s = 0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        if((i * i + j * j) % m == 0):
            s += a[i] * a[j]
print(s)
