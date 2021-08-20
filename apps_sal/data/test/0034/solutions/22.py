(n, a, b) = [int(i) for i in input().split()]
ans = 0
for n1 in range(1, n):
    n2 = n - n1
    x1 = a // n1
    x2 = b // n2
    ans = max(ans, min(x1, x2))
print(ans)
