def fact(k):
    (a, b) = (0, 0)
    while k % 2 == 0:
        k //= 2
        a += 1
    while k % 3 == 0:
        k //= 3
        b += 1
    if k != 1:
        return -1
    return a + b


(n, m) = list(map(int, input().split()))
if n > m or m / n != m // n:
    print(-1)
elif n == m:
    print(0)
else:
    print(fact(m // n))
