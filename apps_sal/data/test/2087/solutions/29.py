a,b,c = map(int,input().split())
p = 998244353
print((a*(a+1)*b*(b+1)*c*(c+1)//8)%p)
