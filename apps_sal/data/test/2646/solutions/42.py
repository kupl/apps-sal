def main():
	N, M = [int(x) for x in input().split(" ")]
	route = [[] for i in range(N)]
	for i in range(M):
		A, B = [int(y) for y in input().split(" ")]
		route[A - 1] += [B]
		route[B - 1] += [A]

	checked = [1] + [0] * (N - 1)
	to_check = [{"src" : s, "dst" : 1} for s in route[0]]
	signal = [-1] + [0] * (N - 1)

	for r in route[0]:
		checked[r - 1] = 1

	while len(to_check) > 0:
		checking = to_check.pop(0)
		src = checking["src"]
		signal[src - 1] = str(checking["dst"])
		rooms = route[src - 1]
		for r in rooms:
			if checked[r - 1] == 0:
				to_check.append({"src": r, "dst": src})
				checked[r - 1] = 1

	if signal.count(0) > 0:
		print("No")
	else:
		print("Yes")
		print("\n".join(signal[1:]))

main()
