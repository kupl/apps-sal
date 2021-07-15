def dfs(i, visited, g):
	indexes = []
	visited.add(i)
	for j in g[i]:
		if j not in visited:
			indexes.extend(dfs(j, visited, g))
	indexes.append(i)
	return indexes

def solve(n, p, g):
	visited = set()
	result = [0] * n
	for i in range(n):
		if i not in visited:
			indexes = dfs(i, visited, g)
			values = [p[i] for i in indexes]

			indexes = sorted(indexes)
			values = sorted(values)

			for j in range(len(indexes)):
				result[indexes[j]] = values[j]
	return result




def main():
	n = int(input())
	p = list(map(int, input().split()))
	swaps = []
	for i in range(n):
		row = input()
		temp = []
		for j in range(n):
			if row[j] == '1':
				temp.append(j)
		swaps.append(temp)
	result = solve(n, p, swaps)
	print(" ".join(map(str, result)))


def __starting_point():
	main()
__starting_point()
