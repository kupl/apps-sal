a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
n = a[0]
m = a[1]
pmin = (n % m) * (n // m + 1) * (n // m) // 2 + (m - n % m) * (n // m) * (n // m - 1) // 2
l = n - m + 1
pmax = l * (l - 1) // 2
print(int(pmin), int(pmax))
