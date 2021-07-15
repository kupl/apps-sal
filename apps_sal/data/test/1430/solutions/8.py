def main():
	N, K = [int(x) for x in input().split(" ")]
	S = list(input())
	cnt = [0] # idx = 0, 2, 4 ... -> handstand
	a = 0
	for i in range(len(S)):
		if S[i] == "0":
			if a % 2 == 0:
				a += 1
				cnt.append(1)
			else:
				cnt[-1] += 1
		elif S[i] == "1":
			if a % 2 == 0:
				cnt[-1] += 1
			else:
				a += 1
				cnt.append(1)
	if S[-1] == "0":
		cnt.append(0)

	if K >= (len(cnt) - 1) / 2:
		print(N)
		return 0

	T = [sum(cnt[:(2 * K + 1)])]
	for i in range(0, len(cnt) - 2 * K - 2, 2):
		T.append(T[-1] - cnt[i] - cnt[i + 1] + cnt[i + 2 * K + 1] + cnt[i + 2 * K + 2])
	print(max(T))

main()
