n,k = [int(i) for i in input().split()]
print((6*n-1)*k)
for a in range(n):
    val = 6*a
    print((val+1)*k,(val+2)*k,(val+3)*k,(val+5)*k)

