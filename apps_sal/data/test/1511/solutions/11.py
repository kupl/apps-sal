def main():
	n, m, k = map(int, input().split())
	M = [0] * n
	for i in range(n):
		M[i] = list(map(int, input().split()))
	bn = [0] * n
	bm = [0] * k
	for t in range(m):
		last = [-1] * k
		cnt = [0] * k
		for i in range(n):
			if bn[i] or not M[i][t]:
				continue
			if bm[M[i][t] - 1]:
				bn[i] = t + 1
			else:
				if last[M[i][t] - 1] != -1:
					bn[last[M[i][t] - 1]] = t + 1
				last[M[i][t] - 1] = i
				cnt[M[i][t] - 1] += 1
		for i in range(k):
			if cnt[i] > 1:
				bm[i] = t + 1
				bn[last[i]] = t + 1
	for i in range(n):
		print(bn[i])
	
main()
