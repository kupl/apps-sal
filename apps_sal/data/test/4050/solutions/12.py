from collections import defaultdict
n = int(input())
nums = [int(x) for x in input().split()]
mapas = [defaultdict(list) for _ in range(n)]
for i, nu in enumerate(nums):
	if i:
		mapas[i] = defaultdict(list, mapas[i-1])
	# print(mapas[i])
	mapas[i][nu] = mapas[i][nu] + [(i+1,i+1)]
	su = nu
	for j in reversed(range(1, i)):
		su += nums[j]
		# if su == -2:
		# 	print(nu, 1+j, i+1, mapas[j-1][su])
		if len(mapas[j-1][su])+1 > len(mapas[i][su]):
			mapas[i][su] = mapas[j-1][su] + [(j+1, i+1)]
	# print(su)
	if i:
		su += nums[0]
		# print(su, mapas[i])
		if len(mapas[i][su]) == 0:
			mapas[i][su] = [(1, i+1)]
	# print(mapas[i])
	# print()
	# mapas[i][su] = max(1, mapas[i][su])
mx, my = -1,-1
# print(mapas[-1])
for x, y in mapas[-1].items():
	if len(y)> my:
		mx, my = x, len(y)
# print(mx, my)
print(my)
# print(mapas[-1][mx])
for a, b in mapas[-1][mx]:
	print(a, b)
