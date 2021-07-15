(n, m, a, b) = list(map(int, input().split()))
ans = min(a * n, b * (n//m) + a * (n % m), b * (n//m) + b)
print(ans)

