n, k = list(map(int,input().split()))
print((6*n-1)*k)
for i in range(0, n): print((6*i+1)*k,(6*i+2)*k,(6*i+3)*k,(6*i+5)*k)
