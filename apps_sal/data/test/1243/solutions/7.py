n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(n):
	k+=a[i]
aver=k//n
h=0
x=0
y=1
s=0
for i in range(n):
  s += aver - a[i]
  h += abs(s)
print(h)

