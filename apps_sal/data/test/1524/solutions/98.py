import math

def main():
	S = list(input())
	ls = len(S)
	RL = []
	rc = 0
	lc = 0
	for i in range(ls):
		if i != ls - 1:
			if S[i] == "R":
				rc += 1
			elif S[i] == "L" and S[i + 1] == "L":
				lc += 1
			elif S[i] == "L" and S[i + 1] == "R":
				lc += 1
				RL.append({
					"right": rc,
					"left": lc
				})
				rc = 0
				lc = 0
		else:
			lc += 1
			RL.append({
				"right": rc,
				"left": lc
			})
	cnt = []
	for i in range(len(RL)):
		rl = RL[i]
		rc = rl["right"]
		lc = rl["left"]
		cnt += ["0"] * (rc - 1)
		cnt += [str(int(lc / 2) + math.ceil(rc / 2))]
		cnt += [str(int(rc / 2) + math.ceil(lc / 2))]
		cnt += ["0"] * (lc - 1)

	print(" ".join(cnt))

main()
