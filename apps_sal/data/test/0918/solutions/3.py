3

class StdIO:
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

io = StdIO()


def main():
	n, m = io.read_ints()

	ppl = [list() for i in range(m)]

	for i in range(n):
		name, reg, score = io.read_strings()
		reg = int(reg)
		score = int(score)
		reg -= 1

		ppl[reg].append((score, name))

	for reg in range(m):
		ppl[reg].sort(reverse=True)

		team = ppl[reg]
		sca = team[0][0]
		scb = team[1][0]
		scc = team[2][0] if len(team) > 2 else None

		if scc is None or (sca > scc and scb > scc):
			print(team[0][1], team[1][1])
		else:
			print('?')

def __starting_point():
	main()

__starting_point()
