import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n, = I()
from bisect import bisect_right as br

l = I() + [MOD]

l.sort()
ans = MOD
for i in range(n):
	k = l[i]
	j = br(l, 2*l[i])
	ans = min(ans, n - (j - i))
print(ans)
