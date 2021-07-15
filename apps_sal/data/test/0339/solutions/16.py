n = int(input())
k = int(input())
a = int(input())
b = int(input())
ans = 0
if k > 1:
    while n > 1:
        new_n = max(1, n // k * k)
        ans += (n - new_n) * a
        n = new_n
        while n % k == 0:
            new_n = n // k
            ans += min((n - new_n) * a, b)
            n = new_n
else:
    ans = (n - 1) * a
print(ans)
