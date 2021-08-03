n, q = list(map(int, input().split()))
nn = (n**2 + 1) // 2
# for y in range(1,n+1):
#    for x in range(1,n+1):
#        if (x+y)%2==0:
#            print( ((y-1)*n+x+1)//2)
#        else:
#            print( nn+((y-1)*n+x+1)//2 )

# n=10**9
# q=10**5
# y,x=10**9,10**9
a = []
kv_n = n * n
pol_n = n // 2
for i in range(q):
    y, x = list(map(int, input().split()))
    if y > pol_n:
        spes = kv_n - (n - y + 1) * n
    else:
        spes = (y - 1) * n
    if (x + y) % 2 == 0:
        a.append(str((spes + x + 1) // 2))
    else:
        a.append(str(nn + (spes + x + 1) // 2))
print('\n'.join(a))
