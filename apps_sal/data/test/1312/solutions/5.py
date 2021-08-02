3

n, m = list(map(int, input().strip().split()))
t = n // m
for x in range(m + 1):
    if x * t + (m - x) * (t + 1) == n:
        ans = [t] * x + [t + 1] * (m - x)
        break
print(' '.join(map(str, ans)))
