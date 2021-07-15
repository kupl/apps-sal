n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i],y[i] = map(int,input().split())
x.sort()
y.sort()
res = (max(x[-1]-x[0],y[-1]-y[0]))**2
print(res)
