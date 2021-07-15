n = int(input())
x, y = list(map(int, input().strip().split()))

if n-x + n-y >= x-1 + y-1:
	print("White")
else:
	print("Black")
