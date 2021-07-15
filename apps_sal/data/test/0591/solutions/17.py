f = open("input.txt", "r")
g = open("output.txt", "w")
n, k = map(int, f.readline().split())
a = [(x+1, int(y)) for x, y in enumerate(f.readline().split())]
a = sorted(a, key=lambda x: x[1])[::-1]
g.write(str(a[k-1][1]) + "\n")
for z in a[:k]:
	g.write(str(z[0]) + " ")
f.close()
g.close()
