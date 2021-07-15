N = int(input())
S = []

for i in range(N):
	S.append(str(input()))
S.sort()
S.append(0)

prev_name = S[0]
cnt = 1
names = []
cnts = []
for i in range(1, N + 1):
	if prev_name == S[i]:
		cnt += 1
	else:
		names.append(prev_name)
		cnts.append(cnt)
		prev_name = S[i]
		cnt = 1
max_cnt = max(cnts)

for i in range(len(names)):
	if cnts[i] == max_cnt:
		print(names[i])
