n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
l = []
for i in range(0,n):
  l.append(abs(a-(t-h[i]*0.006)))
print(l.index(min(l))+1)
