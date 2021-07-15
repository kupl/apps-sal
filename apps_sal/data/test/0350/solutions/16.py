n = int(input())
data = list(map(int, input().split()))
data.sort()
high = data[-1]
ret = 0
for i in range(n-1, -1, -1):
	chosen = min(data[i], high)
	ret += max(chosen, 0)
	high = chosen-1
print(ret)

