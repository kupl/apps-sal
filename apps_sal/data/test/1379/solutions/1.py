n, m, d = list(map(int, input().split()))
breaks = list(map(int, input().split()))

breaks_S = sorted(breaks)
index_s = [i[0] for i in sorted(enumerate(breaks), key=lambda x:x[1])]

d += 1

answer = [-1] * n

x = 1


for i in range(n):
	while True:
		if i >= x and breaks_S[i] - breaks_S[i - x] < d:
			x += 1
		elif n - i > x and breaks_S[i + x] - breaks_S[i] < d:
			x += 1
		else:
			break


for i in range(n):
	answer[index_s[i]] = i % x + 1


print(x)
print(*answer)





