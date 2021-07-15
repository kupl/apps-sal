n = int(input())
a = list(map(int,input().split()))
a.sort()
x = a[:len(a)//2]
y = a[len(a)//2:]
sol = 0
for i,j in zip(y, reversed(x)):
    sol += (i+j)*(i+j)
print(sol)
