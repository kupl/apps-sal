(n, k) = map(int, input().split())
mass = [int(i) for i in input().split()]
mass = mass[::-1]
summ = 0
m = []
for i in range(n - 1):
    summ += mass[i]
    m.append(summ)
m = sorted(m, reverse=True)
print(sum(mass) + sum(m[:k - 1]))
