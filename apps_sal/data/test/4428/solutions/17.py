n = int(input())
l = list(map(int, input().split()))

mx = 0
left = 0
right = n - 1
sl = 0
sr = 0
while left <= right:
	if sl == sr:
		mx = sl
		sl += l[left]
		left += 1
	elif sl > sr:
		sr += l[right]
		right -= 1
	elif sl < sr:
		sl += l[left]
		left += 1
if sl == sr:
	mx = sl
print(mx)
