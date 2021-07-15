n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

maxi = min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
minnie = n-(min(a[0],b[0]+b[2])+min(a[1],b[1]+b[0])+min(a[2],b[2]+b[1]))
print(minnie,maxi)
