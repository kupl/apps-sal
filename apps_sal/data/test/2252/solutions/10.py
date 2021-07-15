n, m = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
for i in range(m):
    l,r,x = [int(x) for x in input().split(" ")]
    smaller = 0
    for i in range(l-1,r):
        if a[i]<a[x-1]:
            smaller += 1
    if smaller == x-l:
        print("Yes")
    else:
        print("No")

