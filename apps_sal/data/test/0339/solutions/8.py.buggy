n = int(input())
k = int(input())
a = int(input())
b = int(input())
ans = 0
if k == 1:
    print((n - 1) * a)
    return
else:
    while n > 1:
        ans += (n % k) * a
        n -= n % k
        if b > (n - n // k) * a:
            print((n - 1) * a + ans)
            return
        else:
            n //= k
            ans += b
print(ans)
