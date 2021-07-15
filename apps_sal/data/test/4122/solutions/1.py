from itertools import accumulate
import math

H, n = map(int, input().split())

d = list(map(int, input().split()))

acc = list(accumulate(d))
per_round = acc[-1]

m = min(acc)

if m >= 0:
	print(-1)
	return

target = -m

if H <= target:
	rounds = 0
elif per_round >= 0:
	print(-1)
	return
else:
	rounds = math.ceil((H - target) / -per_round)

health = H - rounds * -per_round

for i, diff in enumerate(acc):
	cur = health + diff
	if cur <= 0:
		break

minutes = rounds * n + i+1
print(minutes)
