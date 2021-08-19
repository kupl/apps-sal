import math
prime = [2, 3, 5]
for i in range(7, 1001, 2):
    sqi = math.sqrt(i)
    for j in prime:
        if i % j == 0:
            break
        if sqi < j:
            prime.append(i)
            break


def legendre(n, p):
    if n == 0:
        return 0
    else:
        return n // p + legendre(n // p, p)


N = int(input())
power_of_prime = [legendre(N, p) for p in prime]
cnt = 1
for i in range(len(power_of_prime)):
    cnt = cnt * (power_of_prime[i] + 1) % 1000000007
print(cnt)
