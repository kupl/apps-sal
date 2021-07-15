n = int(input())
dis = list([int(x) << 1 for x in input().split()])
ter = input()
st, ans = 0, 0
time = {'G': 5, 'W': 3, 'L': 1}
delta = {'G':1, 'W':1, 'L':-1}
hasWater = False
convert = 0
for i in range(n):
	st += dis[i] * delta[ter[i]]
	ans += dis[i] * time[ter[i]]
	# print('st = %d, ans = %d' % (st, ans))
	if ter[i] == 'W':
		hasWater = True
	elif ter[i] == 'G':
		convert += dis[i]
	if st < 0:
		if hasWater:
			ans += (-st) * 3
		else:
			ans += (-st) * 5
		st = 0
	convert = min(convert, st // 2)
	# print('convert = %d' % convert)
	# print('ans = %d' % ans)
ans -= 4 * convert
ans -= 2 * (st // 2 - convert)
print(ans // 2)



