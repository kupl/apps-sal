alph = 'qwertyuiopasdfghjkl;zxcvbnm,./'
d = {alph[i]: i for i in range(len(alph))}
d1 = input()
res = ''
for c in input():
	res += alph[d[c] + (-1 if d1 == 'R' else 1)]
print(res)
