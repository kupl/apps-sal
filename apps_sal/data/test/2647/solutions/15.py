def main():
	H, W = [int(n) for n in input().split(" ")]
	iniBlack = 0
	S = []
	S.append(["X"] * (W + 2))
	for i in range(H):
		row = list(input())
		iniBlack += row.count("#")
		S.append(["X"] + row + ["X"])
	S.append(["X"] * (W + 2))

	to_visit = [{"row": 1, "col": 1, "step": 1}]
	checked = [[0] * (W + 2) for i in range(H + 2)]
	checked[1][1] = 1

	while len(to_visit) > 0:
		visiting = to_visit.pop(0)
		r0 = visiting["row"]
		c0 = visiting["col"]
		s0 = visiting["step"]
		for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
			r = r0 + d[0]
			c = c0 + d[1]
			if S[r][c] == "." and checked[r][c] == 0:
				to_visit.append({"row": r, "col": c, "step": s0 + 1})
				checked[r][c] = s0 + 1

	if checked[H][W] == 0:
		print(-1)
		return 0
	print(H * W - iniBlack - checked[H][W])

main()
