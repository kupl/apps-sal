m,n = list(map(int,input().split()))

a = [0]*m

for i in range(m):
    k = list(map(int,input().split()))
    for j in range(k[0]):
        a[i] |= 1<<k[j+1]

for i in range(m):
    for j in range(m):
        if a[i]&a[j] == 0:
            print("impossible")
            quit()
print("possible")

