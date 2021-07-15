X, N = map(int, input().split())
ps = list(map(int, input().split()))
bgr, smr = X, X
while bgr <= 100:
	if bgr not in ps:
		break
	bgr += 1
while smr >= 1:
	if smr not in ps:
		break
	smr -= 1
print(bgr) if bgr - X < X - smr else print(smr)

