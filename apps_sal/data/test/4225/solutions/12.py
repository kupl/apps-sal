#ABC167B
a,b,c,k = map(int,input().split())
print(min(a,k)-max(k-a-b,0))
