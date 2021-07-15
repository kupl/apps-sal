n = int(input())
if n < 10:
	print(n)
	return
a = n - int(str(n)[1:]) - 1
b = n - a
a = [*map(int, str(a))]
b = [*map(int, str(b))]
print(sum(a) + sum(b))
