# import sys
# sys.stdin = open('cf599c.in')

n = int(input())
hh = list(map(int, input().split()))
idx = sorted(range(n), key=lambda i: hh[i])

num_blocks = 0
curr_max = idx[0]
for j, i in enumerate(idx):
	curr_max = max(i, curr_max)
	if curr_max <= j:
		num_blocks += 1

print(num_blocks)
