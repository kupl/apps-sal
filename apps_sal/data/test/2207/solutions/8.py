# 690 D1
r,c = [int(i) for i in input().split()]
for i in range(r-1):
	input()
s = input()
segs = 0
prev = '.'
for x in s:
	if x=='B' and prev =='.':
		segs += 1
	prev = x
print(segs)

