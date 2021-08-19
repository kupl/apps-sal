(n, ans) = (int(input()), 0)
for i in range(1, n + 1):
    ans += 1 / i
print('{:.12f}'.format(ans))
