n = int(input())
x = list(map(int,input().split()))
x.sort()
for i in range(n - 1, -1, -1):
	if x[i] < 0:
		print(x[i])
		break
	if x[i] ** 0.5 % 1 != 0:
		print(x[i])
		break

