n = int(input())
k= int(input())
a = int(input())
b = int(input())
res = 0
if k == 1:
    print((n - 1) * a)
else:
    while n != 1:
        res += (n % k) * a
        if b > (n // k)*(k - 1) * a:
            res += (n // k)*(k - 1) * a
        else:
            res += b
        n //= k
        if n < k:
            res += (n - 1) * a
            break
    print(res)
