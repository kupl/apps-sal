n = int(input())
b = list(map(int, input().split()))
cur = 0
cnt = 0
for i in range(n):
	cnt += abs(cur - b[i])
	cur = b[i]
print(cnt)

