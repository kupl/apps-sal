a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if k1 > k2:
    (k1, k2) = (k2, k1)
    (a1, a2) = (a2, a1)
h = (k1 - 1) * a1 + (k2 - 1) * a2
print(max(0, n - h), end=' ')
ans = min(n // k1, a1)
n = max(0, n - ans * k1)
ans += n // k2
print(ans)
