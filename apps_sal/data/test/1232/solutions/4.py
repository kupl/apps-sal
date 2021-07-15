s=input()
k,m=[int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if a[k-1]<b[-m]:
    print("YES")
else:
    print("NO")

