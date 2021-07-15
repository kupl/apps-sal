n = int(input())

av = list(map(int,input().strip().split(' ')))
bv = list(map(int,input().strip().split(' ')))

if sum(av) <= sum(sorted(bv)[-2:]):
	print('YES')
else:
	print('NO')
