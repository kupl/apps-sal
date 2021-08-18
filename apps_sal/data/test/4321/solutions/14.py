n, k = map(int, input().split())
while k:
    k -= 1
    if n >= 10:
        if n % 10:
            n -= 1
        else:
            n //= 10
    else:
        n -= 1
print(n)
