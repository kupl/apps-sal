(n, m) = list(map(int, input().split()))
divisors = []
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        divisors.append(i)
        if i != m // i:
            divisors.append(m // i)
divisors.sort()
print([i for i in divisors if i <= m / n][-1])
