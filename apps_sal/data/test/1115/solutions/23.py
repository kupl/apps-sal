n = int(input())
arr = list(map(int, input().split()))
m = int(input())
moment = []
my = 0
for i in range(m):
	a, b = map(int, input().split())
	moment.append((a, b))
	if b > my:
		my = b
moment = sorted(moment)
total = sum(arr)
if total <= my:
	for a, b in moment:
		if total <= b:
			print(str(max(total, a)))
			break

else:
	print('-1')
