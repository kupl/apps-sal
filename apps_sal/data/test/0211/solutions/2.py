n, corecte, k = list(map(int, input().split()))
incorecte = n - corecte
mod = 10**9 + 9


corecte_consecutive = max(0, n - incorecte * k)
dublari = corecte_consecutive // k
corecte_ramase = corecte - corecte_consecutive


def power(b, exp):
    if exp == 0:
        return 1

    half = power(b, exp // 2)
    if exp % 2 == 0:
        return (half * half) % mod
    return (half * half * b) % mod


score = (power(2, dublari + 1) - 2) * k + corecte_ramase + corecte_consecutive % k

print(score % mod)
