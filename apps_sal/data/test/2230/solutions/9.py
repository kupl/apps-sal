n = int(input())
p = 0
for i in range(n):
    for j in range(int(n/2)):
        p += 1
        print(p,n*n-p+1,end=" ")
    print()

