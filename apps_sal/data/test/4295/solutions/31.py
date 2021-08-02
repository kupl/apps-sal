n, k = list(map(int, input().split()))

n = n % k
abs_n_minus_k = abs(n - k)
ans = n

if n % k == 0:
    ans = 0
else:
    while abs_n_minus_k < n:
        n = abs_n_minus_k
        abs_n_minus_k = abs(n - k)
        ans = n

print(ans)
