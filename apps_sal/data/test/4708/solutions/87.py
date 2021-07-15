n,k,x,y = [int(input()) for i in range(4)]
cost=(min(n,k)*x+max(0,n-k)*y)
print(cost)
