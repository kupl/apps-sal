n=int(input())
a=[int(x) for x in input().split()]

for i in range(n-1):
    if a[i]<a[i+1]:
        a[i+1]-=1
    if a[i]>a[i+1]:
        print("No")
        return
print("Yes")
