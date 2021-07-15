N = int(input())
a = [int(i) for i in input().split()]

suffix = [a[-1]]
tok = [a[-1]]
tol = [0]
best = [a[-1]]

for x in reversed(a[:-1]):
	# keep
	keep = x + suffix[-1] - best[-1]
	give = best[-1]
	best.append(max(keep,give))
	tok.append(keep)
	tol.append(give)
	suffix.append(suffix[-1] + x)

# print(best, tok, tol, suffix)
print(suffix[-1] - best[-1], best[-1])
	



