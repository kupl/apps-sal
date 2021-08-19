(n, m) = tuple(map(int, str.split(input())))
a = list([input() for _ in range(n)])
while n % 2 == 0 and all([a[i] == a[-i - 1] for i in range(n // 2)]):
    n //= 2
    a = a[:n]
print(n)
