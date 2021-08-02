n = int(input())
if n % 2 != 0:
    print(0)
else:
    k = 10
    q = 0
    while k <= n:
        q += n // k
        k *= 5
    print(q)
