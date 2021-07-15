l1, r1, l2, r2, k  = map(int, input().split())
start = max(l1, l2)
end = min(r1, r2)
if start <= k <= end:
	print(end - start)
elif start <= end:
	print(end - start + 1)
else:
	print(0)
