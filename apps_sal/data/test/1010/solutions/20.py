3

n = int(input())
a = list(tuple(map(int, input().split())))

while len(a) > 0 and a[0] == 0:
	a.pop(0)
while len(a) > 0 and a[-1] == 0:
	a.pop()

if len(a) == 0:
	print("0")
else:
	res = 1
	num = 1

	for i in a:
		if i == 0:
			num += 1
		if i == 1:
			res *= num
			num = 1

	print(str(res))

