# 1は除外
# ・N-1の約数は全て対象
# ・Nの約数でsqrt(N)以下の数について、Nで割れなくなるまで割って、最後にあまりが1になればOK
# ・N自身は必ず対象
# これを足し合わせる

N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


# N-1の約数の個数
ans = len(make_divisors(N - 1)) - 1


def check(n, x):
    # xで割った余りがxの倍数でなくなるまでxで割る
    # xの倍数でなくなったときにxで割って1余ればOK
    while n % x == 0:
        n //= x
    return (n % x == 1)


# Nの約数で2以上sqrt(N)以下の数
for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        if check(N, i):
            ans += 1

# N自身も対象
ans += 1

print(ans)
