a,b = map(int,input().split())
c = 0
for i in range(2):
    if a > b:
        c += a
        a -= 1
    elif a < b:
        c += b
        b -= 1
    else:
        c += b
        b -= 1
print(c)
