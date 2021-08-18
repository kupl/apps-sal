n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


ans = 1

for div in make_divisors(sum(a)):
    mod_div = []
    for ai in a:
        mod_div.append(ai % div)
    mod_div.sort()

    tmp_p = n * div - sum(mod_div)
    tmp_m = 0

    for i, x in enumerate(mod_div):
        tmp_m += x
        tmp_p -= div - x
        if tmp_m == tmp_p and tmp_m <= k:
            ans = max(div, ans)

print(ans)
