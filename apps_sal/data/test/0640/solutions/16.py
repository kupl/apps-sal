(a,b) = tuple(map(int,input().split()))
n1 = n2 = 0
for i in (1,2,3,4,5,6):
    r1 = abs(a - i)
    r2 = abs(b - i)
    if r1 < r2:
        n1 += 1
    elif r1 > r2:
        n2 += 1
print(n1,6 - n1 - n2,n2)

