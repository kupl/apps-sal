(n, m) = map(int, input().split())
x = [int(i) for i in input().split()]
x.sort()
if n >= m:
    ans = 0
else:
    x_sa = [x[i + 1] - x[i] for i in range(m - 1)]
    x_sa.sort(reverse=True)
    if n > 1:
        del x_sa[:n - 1]
    ans = sum(x_sa)
print(ans)
