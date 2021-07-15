n, s = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n-1):
    x, y = list(map(int, input().split()))
    a[x-1]+=1
    a[y-1]+=1
counter = 0
for i in a:
    if (i==1):
        counter+=1
print((2*s)/counter)
    

