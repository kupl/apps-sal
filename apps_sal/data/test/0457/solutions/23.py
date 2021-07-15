def factor(x):
    r = set()
    if x % 2 == 0:
        r.add(2)
    while x % 2 == 0:
        x //= 2
    for i in range(3, int(x ** .5 + 2), 2):
        if x % i == 0:
            r.add(i)
        while x % i == 0:
            x //= i
    if x != 1:
        r.add(x)
    return r
a, n = list(map(int, input().split()))
s = factor(a)
sol = 1
for i in s:
    t = i % 1000000007
    m = i
    while m <= n:
        sol = (sol * pow(t, n // m, 1000000007)) % 1000000007
        m = m*i
print(sol)

