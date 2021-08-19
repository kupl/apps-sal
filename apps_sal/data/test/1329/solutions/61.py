def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


N = int(input())
prime = dict()
for i in range(2, N + 1):
    prime_i = factorization(i)
    for (p, num) in prime_i:
        if p in prime:
            prime[p] += num
        else:
            prime[p] = num
divisor_75 = 0
divisor_25 = 0
divisor_15 = 0
divisor_5 = 0
divisor_3 = 0
for v in prime.values():
    if v >= 74:
        divisor_75 += 1
    if v >= 24:
        divisor_25 += 1
    if v >= 14:
        divisor_15 += 1
    if v >= 4:
        divisor_5 += 1
    if v >= 2:
        divisor_3 += 1
ans = 0
ans += divisor_75
ans = max(ans, ans + divisor_25 * (divisor_3 - 1))
ans = max(ans, ans + divisor_15 * (divisor_5 - 1))
ans = max(ans, ans + divisor_5 * (divisor_5 - 1) // 2 * (divisor_3 - 2))
print(ans)
