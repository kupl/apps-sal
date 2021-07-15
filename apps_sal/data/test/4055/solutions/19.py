n = int(input())
a = [int(d) for d in input().split()]
k=0
for x in range(1 , n-1):
    if(a[x-1] == a[x+1] and a[x-1] == 1 and a[x] == 0):
        a[x+1] = 0
        k+=1
print(k)

