import heapq

N,M = map(int,input().split())
b = list(map(int,input().split()))
a = []

for i in range(N):
	a.append((b[i],1))

for i in range(M):
	bb,cc = map(int,input().split())
	a.append((cc,bb))

a.sort()
a.reverse()

#for j in a:
#	print(j)

cnt = 0
ans = 0

for i in range(N):
	if cnt + a[i][1] > N:
		ans += a[i][0]*(N-cnt)
		break

	ans += a[i][0]*a[i][1]
	cnt += a[i][1]

print(ans)
