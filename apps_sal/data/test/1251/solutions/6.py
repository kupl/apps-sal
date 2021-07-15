import sys
oo=1000000000000
ar=[]
def solve(l, r, val):
	if(r<l): return 0
	indx=l+ar[l:r+1].index(min(ar[l:r+1]))
	tot=r-l+1
	cur=ar[indx]-val+solve(l, indx-1, ar[indx])+solve(indx+1, r, ar[indx])
	return min(tot, cur)
sys.setrecursionlimit(10000)
n=int(input())
ar=list(map(int, input().split()))
print(solve(0, n-1, 0))
