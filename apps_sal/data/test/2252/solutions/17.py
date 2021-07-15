n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
d = dict()
for _ in range(m):
    l,r,x = list(map(int,input().split()))
    if x > r or x < l:
        print("Yes")
    else:
        b = a[l-1:r]
        res = 0
        for item in b:
            if item < a[x-1]:
                res += 1
        if res == x-l:
            print("Yes")
        else:
            print("No")
    

