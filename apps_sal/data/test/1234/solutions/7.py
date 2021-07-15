import bisect

n, m, k = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))

new_array = [(v, idx) for idx, v in enumerate(array)]
new_array.sort()

to_select = new_array[-m*k:]

to_select = [(b, a) for a, b in to_select]
to_select.sort()

res = 0
curr_m = 0
partitions = []
for pos, val in to_select:
	res += val
	curr_m += 1
	if curr_m == m:
		partitions.append(str(pos+1))
		curr_m = 0


print(res)
print(" ".join(partitions[:-1]))


