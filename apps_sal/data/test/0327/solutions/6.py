n, k= list(map(int,input().split()))

r = 0
nn = n
while nn:
    nn >>= 1
    r += 1

print((1<<r)-1 if k>1 else n)

