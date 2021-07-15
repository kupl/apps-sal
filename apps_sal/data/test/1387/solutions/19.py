def main():
	n, t = list(map(int, input().split()))	
	a =[0] + list(map(int, input().split())) + [100000]
	d = {}
	for i in range(1,n):
		d[i] = i + a[i]
	reached = True
	i = 1
	count = 1
	while reached and count <= 100009:
		if i in d:
			if d[i] == t:
				print ('YES')
				return
			i = d[i]
			count += 1
		else:
			break
	print('NO')



	

def __starting_point():
	main()

__starting_point()
