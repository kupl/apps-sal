import numpy as np

N=int(input())
V=np.array(list(map(int,input().split())))
C=np.array(list(map(int,input().split())))

P=V-C

ans = 0
for i in P:
	if i>=0:
		ans += i

print(ans)
