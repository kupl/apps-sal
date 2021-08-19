def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


(s, p) = map(int, input().split())
a = make_divisors(p)
ans = 0
for i in range(len(a)):
    b = p // a[i]
    if b + a[i] == s:
        ans += 1
        break
if ans == 0:
    print('No')
else:
    print('Yes')
