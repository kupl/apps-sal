import sys

def norm(num):
	if num < 10:
		return '0' + str(num)
	else:
		return str(num)

h, m = [int(x) for x in input().split(':')]
diff = int(input())

hdiff = diff // 60
mdiff = diff % 60

mans = m + mdiff
hans = (h + hdiff) % 24
hans = (hans + 1) % 24 if mans >= 60 else hans
mans %= 60
s = norm(hans) + ':' + norm(mans)

print(s)

