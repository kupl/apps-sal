N,X,T=map(int,input().split())

a = N // X
if N % X == 0:print(a * T)
else:print((a+1)*T)
