n, t, k, d = list(map(int, input().split()))
n = (n // k) + (1 if n % k else 0)
# if d % t != 0:
#     d += t - d % t

# print(n, d, t)
print("YES" if d < (n - 1) * t else "NO")

