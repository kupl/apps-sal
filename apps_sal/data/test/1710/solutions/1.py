n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ones_ser_ie = [0 for _ in range(n)]
cur_ones_ser_ie = 0
ones_in_tail_i = 0
for i in reversed(list(range(n))):
	if a[i] == 1:
		ones_in_tail_i += 1
		cur_ones_ser_ie += 1
	else:
		cur_ones_ser_ie = 0
	ones_ser_ie[i] = cur_ones_ser_ie


res = 0
for i in range(n):
	p = 1
	s = 0
	j = i
	ones_in_tail_j = ones_in_tail_i
	while j < n:
		if a[j] == 1:
			cur_ones_ser_ie = ones_ser_ie[j]
			if p % k == 0 and 1 <= p//k-s <= cur_ones_ser_ie:
				res += 1
			ones_in_tail_j -= cur_ones_ser_ie
			s += cur_ones_ser_ie
			j += cur_ones_ser_ie
		else:
			p *= a[j]
			s += a[j]
			if p == s * k:
				res += 1
			elif p > (s + ones_in_tail_j) * k:
				break
			j += 1
	if a[i] == 1:
		ones_in_tail_i -= 1
print(res)

