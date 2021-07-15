X,Y = map(int,input().split())
k = 1
a = X
while a<=Y:
    a = a*2
    k += 1
print(k-1)
