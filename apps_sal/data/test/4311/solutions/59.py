n = int(input())
c = 1
x = []
x.append(n)
while True:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+1
    c+=1
    if n in x:
        break
    x.append(n)
print(c)
