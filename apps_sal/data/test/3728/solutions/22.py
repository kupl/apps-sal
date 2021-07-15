def get_perms(perm):
	perms = {tuple(perm)}
	for i in range(len(perm)):
		for j in range(i+1, len(perm)):
			perm_copy = list(perm)
			perm_copy[i], perm_copy[j] = perm_copy[j], perm_copy[i]
			perms.add(tuple(perm_copy))
	return perms

n, m = list(map(int, input().split(' ')))
good_perms = get_perms([i for i in range(1, m+1)])
for i in range(n):
	perm = list(map(int, input().split(' ')))
	good_perms &= get_perms(perm)
if good_perms:
	print('YES')
else:
	print('NO')

