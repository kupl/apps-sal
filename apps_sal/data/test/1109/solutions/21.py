n, k = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
l = [0] * k
for i in range(k):
	l[i] = v[i::k].count(1)
ans = 0
n //= k
for x in l:
	ans += min(x, n - x)
print(ans)

