def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


n = int(input())
l = [i for i in range(n + 1)]
ls = l[1::2]
ans = 0
for i in ls:
    if len(make_divisors(i)) == 8:
        ans += 1
print(ans)
