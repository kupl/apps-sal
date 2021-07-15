M, K = map(int, input().split())

if M == 0:
	if K == 0:
		print(0, 0)
	else:
		print(-1)
	return

if M == 1:
	if K == 0:
		print(0, 0, 1, 1)
	else:
		print(-1)
	return

N = 2 ** M
if N <= K:
	print(-1)
	return

ans = []
ans.append(K)

for i in range(N):
	if i == K:
		continue
	ans.append(i)

ans.append(K)

for i in range(N-1, -1, -1):
	if i == K:
		continue
	ans.append(i)

for i in ans:
	print(i, end=' ')
