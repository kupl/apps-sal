A,B,N=map(int,input().split());f=lambda x:int(A*x/B)-A*int(x/B);print((A>1)*(B>1)*f(min(N,B-1)))
