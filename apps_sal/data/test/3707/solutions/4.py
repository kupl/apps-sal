n, t, k, d = list(map(int, input().split()))

p = (d // t) * k
if n - p > k:
    print("YES")
else:
    print("NO")
