pht, pa, phl = map(int, input().split())
bht, ba = map(int, input().split())

st = []
while bht > 0:
	if pht <= ba and bht > pa:
		st += ['HEAL']
		pht += phl
	else:
		bht -= pa
		st += ['STRIKE']
	pht -= ba

print(len(st))
print('\n'.join(st))
