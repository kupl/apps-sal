A, B, C, D = [int(i) for i in input().split()]

count_ymz = [None for i in range(D-B + 1)]
for i in range(len(count_ymz)):
	count_ymz[i] = min(C, D-i) - max(C-i, B) + 1

pre_count_ymz = [None for i in range(len(count_ymz))]
pre_count_ymz[0] = count_ymz[0]
for i in range(1, len(count_ymz)):
	pre_count_ymz[i] = pre_count_ymz[i-1] + count_ymz[i]
ans = 0
for x in range(A, B+1):
	if x > D-B + 1:
		ans += pre_count_ymz[-1]
	else:
		ans += pre_count_ymz[x-1]

print(ans)
