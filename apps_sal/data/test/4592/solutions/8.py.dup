import math

n = int(input())
if n == 1:
    print((1))
    return
dp = [0] * (n + 1)
mod = 10**9 + 7


def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial):
            input_list[s] = False


prime = sieve_of_erastosthenes(1000)
prime = [i for i, t in enumerate(prime) if t]

for i in range(2, n + 1):
    v = i
    while v < n + 1:
        dp[i] += 1
        v += i

dp2 = [0] * (n + 1)
for p in prime:
    v = p
    k = 1
    while v < n + 1:
        dp2[p] += dp[v]
        v *= p
        k += 1

ans = 1
for i in range(n + 1):
    ans = (ans * (dp2[i] + 1)) % mod
print(ans)
