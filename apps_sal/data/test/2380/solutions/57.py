def main():
	N, M = [int(x) for x in input().split(" ")]
	A = [int(a) for a in input().split(" ")]
	A.sort()
	overwrite = []
	for i in range(M):
		B, C = [int(x) for x in input().split(" ")]
		overwrite.append({
			"count": B,
			"number": C
		})
	overwrite.sort(key=lambda o: -o["number"])
	j = 0
	k = 0
	flag = False
	while not flag and j < len(A) and k < len(overwrite):
		o = overwrite[k]
		for m in range(o["count"]):
			if j < len(A) and A[j] <= o["number"]:
				A[j] = o["number"]
				j += 1
			else:
				flag = True
		k += 1

	print((sum(A)))

main()

