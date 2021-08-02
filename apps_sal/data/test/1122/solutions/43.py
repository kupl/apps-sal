n, m = list(map(int, input().split()))

a = n // 2
b = a + 1
abset = set()

for i in range(m):
    print(a, b)
    abset.add(b - a)
    abset.add(n - b + a)
    a -= 1
    b += 1
    if n % 2 == 0 and (b - a == abs(n - b + a) or b - a in abset or n - b + a in abset):
        b += 1
