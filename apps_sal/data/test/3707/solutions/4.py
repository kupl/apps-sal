n, t, k, d = list(map(int, input().split()))

# t1 = (n // k + n % k == 0 ? 0 : 1) * t
p = (d // t) * k
if n - p > k:
	print("YES")
else:
	print("NO")
