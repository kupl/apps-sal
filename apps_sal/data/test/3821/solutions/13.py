
def __starting_point():
	N = int(input())
	probs = list(map(float, input().split()))
	probs.sort()
	P, S = 1.0, 0.0
	sol = 0.0
	for n in reversed(range(N)):
		# print(probs[n])
		if probs[n] == 1.0:
			sol = 1.0
			break
		if S > 1:
			# print(S + (probs[n]/(1 - probs[n])))
			break
		P, S = P*(1 - probs[n]), S + probs[n]/(1 - probs[n])
		# print(P, S, P*S)
		sol = P*S
	print(sol)
__starting_point()
