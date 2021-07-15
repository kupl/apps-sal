n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans, near = 0, 10**5
for i, high in enumerate(h):
	temp = abs(a - (t - high * 0.006))
	if near > temp:
		near = temp
		ans = i + 1
print(ans)
