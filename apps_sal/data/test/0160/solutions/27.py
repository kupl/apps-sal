N, K = map(int, input().split())
A = list(map(int, input().split()))


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


D = make_divisors(sum(A))
ans = 1
for i in D:
    E = []
    for j in A:
        d = j % i
        if d != 0:
            E.append(d)
    if len(E) == 0:
        ans = i
    E = sorted(E)
    cn = 0
    e = sum(E)
    left, right = e, 0
    for k in range(len(E)):
        left -= E[-1 - k]
        right += (i - E[-1 - k])
        if left == right:
            if left <= K:
                ans = i
            break
print(ans)
