import sys
n, m = list(map(int,input().split()))
if (m%n):
	print(-1)
	return
u = m//n;
cnt = 0;
while (u % 2 == 0):
	u //=2
	cnt += 1
while (u % 3 == 0):
	u //=3
	cnt += 1
print(cnt if u == 1 else -1)

