from scipy.special import comb


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
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


n, m = map(int, input().split())
a = factorization(m)
M = 10**9 + 7

ans = 1
if m == 1:
    print(1)
    return
for i in a:
    ans *= comb(n, i[1], exact=True, repetition=True)
    ans = ans % M
print(ans)
