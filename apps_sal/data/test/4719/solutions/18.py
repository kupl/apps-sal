from collections import Counter
n = int(input())
s = [''] * n
for i in range(n):
	s[i] = input()

r = s[0]
for i in range(1, n):
	set_c = set(r) & set(s[i])
	if len(set_c) == 0:
		print('')
		return
	next_r = ''
	cnt_r = Counter(r)
	cnt_s = Counter(s[i])
	for c in set_c:
		next_r += c * min(cnt_r[c], cnt_s[c])
	r = next_r
print(''.join(sorted(r)))
