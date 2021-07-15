def int_map():
	return list(map(int, input().split(' ')))

n, k = int_map()

q = n // 2

a = q // (k+1)

print(a, k*a, n-(k+1)*a)



