n, w = list(map(int, input().split()))
a = list(map(int, input().split()))

s = 0
min_s = 10000000
max_s = -10000000

for i, e in enumerate(a):
	s += e

	min_s = min(s, min_s)
	max_s = max(s, max_s)

if -min_s > w:
	print(0)
	quit()

if max_s > w:
	print(0)
	quit()

if max_s >= 0 and min_s >= 0:
	max_s = w - max_s + 1
elif max_s >=  0 and min_s < 0:
	max_s = w - max_s + min_s + 1
elif max_s < 0:
	max_s = w + min_s + 1



if max_s < 0:
	print(0)
else:
	print(max_s)
