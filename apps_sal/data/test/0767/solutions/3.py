n, z = list(map(int, input().split()))
l = list(map(int, input().split()))
l = sorted(l)
wyn = 0
maly = 0
duzy = n // 2
zaj = [0] * n
while duzy < n:
	while maly < n:
		if zaj[maly] == 1:
			maly += 1
		else:
			break
	if l[duzy] - l[maly] >= z and zaj[duzy] == 0 and zaj[maly] == 0:
		wyn += 1
		maly += 1
		zaj[maly - 1] = 1
		zaj[duzy] = 1
	duzy += 1
print(wyn)
