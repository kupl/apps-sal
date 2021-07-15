A,B,C,X,Y = map(int,input().split())
ans = 10**10
for k in range(max(X,Y)+1):
    i = max((X-k),0)
    j = max((Y-k),0)
    price = A*i + B*j + C*2*k
    ans = min(ans,price)

print(ans)
