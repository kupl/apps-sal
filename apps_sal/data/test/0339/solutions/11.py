n = int(input())
k = int(input())
a = int(input())
b = int(input())

r = 0

if k == 1:
    print((n - 1) * a)
    return

while n != 1:
    if n % k != 0:
        r += n % k * a
        n -= n % k
    elif n < k:
        r += (n - 1) * a
        n = 1
    else:
        if n // k * (k - 1) * a < b:
            r += n // k * (k - 1) * a
        else:
            r += b
        n //= k
print(r)

