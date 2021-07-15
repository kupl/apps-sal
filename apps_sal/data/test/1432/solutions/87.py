n = int(input())
a = list(map(int,input().split()))

x = [0]*n
for i in range(n):
    x[0] += (-1)**(i) * a[i]
    
for i in range(1,n):
    x[i] = 2*a[i-1] - x[i-1]
    
for i in range(n):
    print(x[i],end="")
    print(" ",end="")
