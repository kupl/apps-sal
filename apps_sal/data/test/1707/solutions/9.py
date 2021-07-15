n = int(input())
a = list(map(int,input().split()))
a = sorted([abs(x) for x in a])


total = 0
i = 0
for j,h in enumerate(a[:-1]):
    h *= 2
    while i<(n-1) and a[i+1]<=h:
        i+=1
    total += i-j
print (total)



