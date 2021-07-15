3

class StdReader:
	def read_int(self):
		return int(self.read_string())

	def read_ints(self, sep=None):
		return [int(i) for i in self.read_strings(sep)]

	def read_float(self):
		return float(self.read_string())

	def read_floats(self, sep=None):
		return [float(i) for i in self.read_strings(sep)]

	def read_string(self):
		return input()

	def read_strings(self, sep=None):
		return self.read_string().split(sep)

reader = StdReader()


def add_e(adj, elist, i, j):
	adj[i].append(j)
	adj[j].append(i)
	elist.append((i, j))


def main():
	n, td, th = reader.read_ints()

	if td > 2 * th or (n > 2 and td == 1):
		print(-1)
		return

	adj = [list()]*n
	elist = []
	d = h = 0

	# depth_v = None
	last_v = 0
	mother_v = 0
	if td == th:
		mother_v = 1

	dst = [0]*n
	dst[0] = th

	for i in range(1, n):
		if h < th:
			add_e(adj, elist, last_v, i)
			last_v = i
			h += 1
			d += 1
			dst[i] = th - h
			if h == th:
				last_v = 0
		elif d < td:
			add_e(adj, elist, last_v, i)
			last_v = i
			d += 1
			dst[i] = d
			# if d == td:
			# 	last_v = 0
		else:
			add_e(adj, elist, mother_v, i)

	for e in elist:
		print(e[0] + 1, e[1] + 1)


def __starting_point():
	main()

__starting_point()
