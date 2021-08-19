
n, m = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


b = make_divisors(m)
# print(b)
a = m // n
# print(a)
ans = 0
for i in b:
    if i <= a:
        ans = i
print(ans)
