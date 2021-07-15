cnt = [int(input()) for _ in range(4)]

if cnt[0] != cnt[3]:
	print(0)
elif cnt[2] > 0 and cnt[0] == 0:
	print(0)
else:
	print(1)

