t = int(input())
while(t > 0):
    t = t - 1
    n = int(input())
    a = input().split()
    b = []
    for i in range(0, n):
        a[i] = int(a[i])
        b.append(a[i])
    b.sort()
    q = 0
    mi = b[0]
    for i in range(0, n):
        if(b[i] % mi != 0):
            if(a[i] != b[i]):
                q = 1
                break
    if(q == 0):
        print("YES")
    else:
        print("NO")
