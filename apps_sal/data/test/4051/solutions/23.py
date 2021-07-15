n = int(input())
a = [int(i) for i in input().split()]
while len(a)!=1:
    
    m = a[0]
    im = 0
    for i in range(1,len(a)):
        if abs(a[i] - a[i-1])>=2:
            print("NO")
            return
        if a[i]>m:
            m = a[i]
            im = i
    a.pop(im)
print("YES")
