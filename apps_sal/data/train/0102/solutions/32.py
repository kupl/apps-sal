t = int(input())
for j in range(t):
    n = int(input())
    n1 = str(n)
    a = 0
    while n // 10:
        a += 9
        n = n // 10
    a += n - 1
    if str(n) * len(n1) <= n1:
        a += 1
    print(a)
