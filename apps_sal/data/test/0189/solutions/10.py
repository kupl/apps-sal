n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 8
ansi = 0
for i in range(1, 101):
	tmp = sum(min(abs(i - t - 1), abs(i - t + 1), abs(i - t)) for t in a)
	if tmp < ans:
		ans = tmp
		ansi = i
print(ansi, ans)
