n,t = list(map(int,input().split())) 
data = list(map(int,input().split()))
s=sum(data)
print('YES' if t==n-1+s else 'NO')

