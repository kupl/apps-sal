n, w = map(int, input().split())
a = list(map(int, input().split()))
mx, mn, bal = 0, 0, 0
for aa in a:
	bal += aa
	mx, mn = max(mx, bal), min(mn, bal)
left, right = - mn, w - mx
if right < 0 or left > right:
	print(0)
else:
	print(right - left + 1)
