w, m, k = map(int, input().split())
w //= k

pre = 0
cur = 9
len = 1
saved_m = m
while m > cur:
	pre += cur * len
	m -= cur
	cur *= 10
	len += 1
pre += (m - 1) * len

w += pre

ans = 0
cur = 9
len = 1
while w > cur * len:
	w -= cur * len
	ans += cur
	cur *= 10
	len += 1
ans += w // len

print(ans - saved_m + 1)
