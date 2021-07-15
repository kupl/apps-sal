def solve(n,items):
	grp_items = [0]*8
	for item in items:
		grp_items[item] += 1

	if (grp_items[1] == n/3 and
		grp_items[5] == 0 and
		grp_items[7] == 0 and
		grp_items[2] == (grp_items[4] + grp_items[6]-grp_items[3]) and
		grp_items[6] >= grp_items[3]):
			while grp_items[1] > 0:
				if grp_items[3] > 0:
					print('1 3 6')
					grp_items[6] -= 1
					grp_items[3] -= 1
				elif grp_items[2] > 0:
					if grp_items[6] > 0:
						print('1 2 6')
						grp_items[6] -= 1
					elif grp_items[4] > 0:
						print('1 2 4')
						grp_items[4] -= 1
					else:
						print(-1) #something wrong in algorithm
					grp_items[2] -= 1
				else:
					print(-1) #something wrong in algorithm

				grp_items[1] -= 1
	else:
		print(-1)


def __starting_point():
	n = int(input())
	items = list(map(int,input().split(' ')))
	solve(n,items)

__starting_point()
