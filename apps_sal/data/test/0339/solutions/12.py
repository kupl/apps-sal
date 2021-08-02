n = int(input())
k = int(input())
a = int(input())
b = int(input())
ans = 0
if ((k == 1) | (k > n)) & (n != 1):
    ans = n * a - a
    n = 1
while (n != 1):
    if (n % k == 0):
        t = n // k
        y = n - t
        if (y * a <= b):
            ans += n * a - a
            n = 1
        else:
            ans += b
            n = t
    else:
        ans += (n % k) * a
        n -= n % k
print(ans)
