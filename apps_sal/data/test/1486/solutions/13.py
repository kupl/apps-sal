n = int(input())
a = [int(x) for x in input().split()]
for i in range(len(a)):
	if i == 0:
		print(abs(a[i] - a[i+1]), abs(a[i] - a[-1]))
	elif i == len(a) - 1:
		print(abs(a[i] - a[i-1]), abs(a[i] - a[0]))
	else:
		print(min(abs(a[i] - a[i-1]), abs(a[i] - a[i+1])), max(abs(a[i] - a[0]), abs(a[i] - a[-1])))
