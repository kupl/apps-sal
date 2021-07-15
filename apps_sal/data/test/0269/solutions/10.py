S = input()
rda = [0]*4
for i, c in enumerate(S):
	if c != '!':
		rda[i%4] = ord(c)
gb = [0]*256
for i, c in enumerate(S):
	if c == '!':
		gb[rda[i%4]] += 1
ans = [gb[ord('R')], gb[ord('B')], gb[ord('Y')], gb[ord('G')]]
print(' '.join(map(str, ans)))

