n,k, x = [int(i) for i in input().split()]
a=[int(i) for i in input().split()]
w=[]
i=0
while i< k:
    a.sort()
    w = a.copy()
    for j in range(0, n, 2):
        a[j]=a[j]^x
    if n * k > 500000 and min(a) == w[0] and max(a) == w[-1]:
        break
    i += 1
print(max(a), min(a))

