n,k,t = [int(i) for i in input().split()]
if t < k:
    print(t)
elif t > n:
    print(k-t+n)
else:
    print(k)
