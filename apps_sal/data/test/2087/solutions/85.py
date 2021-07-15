a,b,c = map(int,input().split())
ans = a*(a+1)//2 * b*(b+1)//2 * c*(c+1)//2
print(ans%998244353)
