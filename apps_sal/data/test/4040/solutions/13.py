n,m,d = map(int,input().split())
c = list(map(int,input().split()))
sc = sum(c)
if sc + (len(c)+ 1) * (d - 1) < n:
    print("NO")
else:
    print("YES")
    ko = n - sc
    for i in range(m):
        if ko != 0:
            if ko >= d - 1:
                print("0 " * (d -1 ), end = "")
                ko -= d -1
            else:
                print("0 " * (ko ), end = "")
                ko = 0
        print((str(i + 1) + " ") * c[i], end = "")
    print("0 " * (ko ), end = "")

