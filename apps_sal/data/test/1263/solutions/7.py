from sys import stdin,stdout
Pi = lambda x: stdout.write(str(x) + '\n')
Ps = lambda x: stdout.write(str(x))
S = lambda x: x*(x+1) // 2
I = lambda x: 1+(2*x)
R = lambda:stdin.readline()
Ri = lambda x:list(map(int,x.split()))
Rs = lambda x:list(map(str,x.split()))
Rf = lambda x:list(map(float,x.split()))
MaxN = int(1e5) + 10
# dp,A = []
def f(i,x,n,k,dp,A,B):
	if i==n:
		if x==0:return 0
		return -1000000
	if dp[i][x+MaxN]!=-1:return dp[i][x+MaxN]
	op1 = f(i+1, x+A[i]-B[i]*k,n,k,dp,A,B)+A[i]
	op2 = f(i+1, x,n,k,dp,A,B)
	dp[i][x+MaxN] = max(op2,op1)
	return dp[i][x+MaxN]
	
def main():	
	# t = int(R())
	for x in stdin:
		n,x = Ri(x)
		A = list(Ri(R()))
		B = list(Ri(R()))
		dp = []
		for i in range(110):
			dp.append([-1]*(MaxN*2))
		ans = f(0,0,n,x,dp,A,B)
		if ans < 1:ans = -1
		Pi(ans)





def __starting_point():
	main()

# 60 == 360

__starting_point()
