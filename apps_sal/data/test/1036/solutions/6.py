n,k=map(int,input().split())
s=input()
import sys
sys.setrecursionlimit(10**5)
memo=[[None for i in range(k+1)]for j in range(n)]
def f(x,y):
	if memo[x][y]!=None:
		return memo[x][y]
		
	if y==0:
		ans=s[x]
	else:
		l=f(x,y-1)
		r=f((x+(2**(y-1)))%n,y-1)
		p=set([l,r])
		if len(p)==1:
			ans=l
		elif "R" not in p:
			ans="S"
		elif "S" not in p:
			ans="P"
		else:
			ans="R"
	memo[x][y]=ans
	return ans
print(f(0,k))
