import sys

N, M = map(int, input().split())
S = input()
tmp = 0
for i in range(N+1):
	if S[i] == '1':
		tmp += 1
		if tmp == M:
			print(-1)
			return
	else:
		tmp = 0

ans = []

i = N
while i > M:
	ind = S[i-M:i].find('0')
	ans.append(M-ind)
	i -= M - ind

ans.append(i)

print(*ans[::-1])
