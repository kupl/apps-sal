n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

yakusu = make_divisors(n)
l_yakusu = len(yakusu)
idx = 0

mx = 10

for a in range(1,10**5+1):
    if a>n:
        break
    if idx<l_yakusu and a==yakusu[idx]:
        idx += 1
        keta_a = len(str(a))
        keta_b = len(str(n//a))
        f = max(keta_a, keta_b)
        mx = min(mx, f)

print(mx)
