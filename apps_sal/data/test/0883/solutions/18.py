n = int(input())
s = sum(int(x) for x in input().split())
ans = 0
for i in range(5):
	if (s + i) % (n + 1):
		ans += 1
print(ans)

