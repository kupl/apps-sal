(n, m, a, b) = list(map(int, input().split()))
if float(a) < float(b) / m:
    ans = a * n
else:
    (n_big, rest) = divmod(n, m)
    ans = n_big * b + min(rest * a, b)
print(ans)
