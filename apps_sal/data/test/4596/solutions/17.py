n = int(input())
a = list(map(int,input().split()))

def devide(a,c,n):
    even = True
    for i in range(n):
        if a[i] % 2 != 0:
           even = False
        else:
            a[i] = int(a[i] / 2)
    return devide(a,c+1,n) if even else c
print(devide(a,0,n))
