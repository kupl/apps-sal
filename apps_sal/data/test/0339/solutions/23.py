n = int(input())
k = int(input())
a = int(input())
b = int(input())
ans = 0
while n != 1:
    if n % k == 0:
        d = n // k
        if b >= (n - d) * a:
            ans += (n - 1) * a
            n = 1
        else:
            ans += b
            n = d
    else:
        r = n % k
        ans += r * a
        n = n - r
print(ans)
