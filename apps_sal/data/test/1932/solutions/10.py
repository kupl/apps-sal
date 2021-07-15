def main():
	n = int(input())

	d = {}
	d['Tetrahedron'] = 4
	d['Cube'] = 6
	d['Octahedron'] = 8
	d['Dodecahedron'] = 12
	d['Icosahedron'] = 20

	ans = 0
	for i in range(n):
		t = input()
		ans += d[t]

	print(ans)
	return

def __starting_point():
	main()
__starting_point()
