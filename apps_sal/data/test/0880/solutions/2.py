n = int(input())
mass = [n]
mass1 = [1]
for i in range(2, n + 1):
    mass1.append((mass1[-1] * i) % 998244353)
for i in range(n - 1, 0, -1):
    mass.append((mass[-1] * i) % 998244353)
summ = mass1[-1]
mass.reverse()
for i in range(n - 1):
    summ += mass[i + 1] * (mass1[i] - 1)
    summ % 998244353
print(summ % 998244353)
