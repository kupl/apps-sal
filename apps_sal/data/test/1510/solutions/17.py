n, m = list(map(int, input().split()))
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse = True)
ans = 0
#print(a, b)
for i in range(min(n, m)):
	ans += max(0, b[i] - a[i])

print(ans)

