def p_factorize(n):
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


MOD = 10 ** 9 + 7
N = int(input())
if N == 1:
    print(1)
else:
    prime = {}
    for i in range(2, N + 1):
        for (p, n) in p_factorize(i):
            try:
                prime[p] += n
            except KeyError:
                prime[p] = n
    ans = 1
    for n in prime.values():
        ans *= n + 1
        ans %= MOD
    print(ans)
