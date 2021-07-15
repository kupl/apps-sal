n = int(input())
Sum = 0
for i in range(n):
	x1, y1, x2, y2 = map(int, input().split())
	S = (x2 - x1 + 1) * (y2 - y1 + 1)
	Sum += S
print(Sum)
