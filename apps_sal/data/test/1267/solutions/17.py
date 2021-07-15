n = int(input())
a = list(map(int,input().split()))
un = 0
a.sort()
for i in range(n):
    if a[i]>0 and (i==0 or a[i]>a[i-1]):
        un += 1
print(un)

