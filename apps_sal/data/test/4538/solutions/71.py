import math
N, D = list(map(int, input().split()))
cnt = 0
for i in range(N):
	X, Y = list(map(int, input().split()))
	if D >= math.sqrt(X ** 2 + Y ** 2):
		cnt += 1
print(cnt)

