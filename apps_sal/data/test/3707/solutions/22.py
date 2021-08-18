n, t, k, d = list(map(int, input().split()))
n = (n // k) + (1 if n % k else 0)

print("YES" if d < (n - 1) * t else "NO")
