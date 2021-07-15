n = int(input())
A=list(map(int,input().split()))
x=0
for i in A:
       x+=i
if not x%n:
    print(n)
else:
    print(n-1)
