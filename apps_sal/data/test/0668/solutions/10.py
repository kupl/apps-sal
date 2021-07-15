n = int(input())
mes = [[int(m), idx] for idx, m in enumerate(input().split(), 1)]
if sum(m[0] for m in mes) < n - 1 or not mes[0][0]:
	print(-1)
	return

mes = [mes[0]] + sorted(mes[1:], reverse=True)

cur = 0
print(n - 1)
for i in range(1, n):
	while not mes[cur][0]:
		cur += 1
	print(mes[cur][1], mes[i][1])
	mes[cur][0] -= 1

