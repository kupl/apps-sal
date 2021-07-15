
n = int(input())
p = list(map(int,input().split()))

r = list(range(n))
l = list(range(n))
I = [-1] * (n+1)

for i,P in enumerate(p):
	I[P] = i
#I[1~Nまでの数字] = 0,1,...
#index を求めている
ans  = 0

for N,index in enumerate(I[1:],1):#1からスタート
	L = index -1
	if L >= 0:
		L = l[L]

	R = index + 1
	if  R < n:
		R = r[R]

	l[R-1] = L
	r[L+1] = R
#0 <= L , R < n
	if L >= 0:
		L2 = L-1
		if L2 >= 0:
			L2 = l[L2]
		ans += N * (L-L2) * (R - index)

	if R < n:
		R2 = R+1
		if R2 < n:
			R2 = r[R2]
		ans += N * (index - L ) * (R2 - R)
print(ans)

