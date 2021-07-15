from math import floor

def main():
	n = int(input())
	a = list(map(int, input().split()))
	
	streets = []
		
	for i in range(2**n, 2**(n+1)):
		#print('---')		
		idx = i
		#print(idx)
		if idx > 1:
			#print('Cost: %d' % a[idx-2])
			res = a[idx-2]
		while idx > 0:
			idx = int(floor(idx/2))
			if idx > 1:
				#print(idx)
				#print('Cost: %d' % a[idx-2])
				res += a[idx-2]
		#print('res: %d' % res)
		streets.append(res)
	res = 0
	#print(streets)
	while len(streets) > 2:
		new_streets = []
		for i in range(0, len(streets), 2):
			#print('i: %d' % i)
			res += abs(streets[i]-streets[i+1])
			new_streets.append(max(streets[i], streets[i+1]))
		#print(new_streets, cur_diff)
		streets = new_streets
	print(res+abs(streets[0]-streets[1]))

def __starting_point():
	main()

__starting_point()
