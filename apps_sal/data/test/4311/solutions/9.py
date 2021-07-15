n = int(input())
c = 0
x = []
while True:
    c+=1
    if n in x:
        print(c)
        break
    x.append(n)
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+1
