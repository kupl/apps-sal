n = int(input())
a = []
k = 0
for i in range(0,n):
    a.append(list(map(int,input().split())))
for i in range(0,n):
    for j in range(0,n):
        if(i!=j):
            if(a[i][0] == a[j][1]):
                k += 1
print(k)
