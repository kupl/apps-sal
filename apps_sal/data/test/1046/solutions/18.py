from collections import Counter
n = int(input())
cnt = Counter(int(x) for x in input().split())
ans = 0
for (a, b) in list(cnt.items()):
	if a:
		if b == 2:
			ans += 1
		if b > 2:
			print(-1)
			return
print(ans)

