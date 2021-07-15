n,k = map(int,input().split())
a = 0
a2 = 0
for i in range(1,n+1):
    if i % k == 0:
        a += 1
    elif 2*i % k == 0:
        a2 += 1
print(a**3 + a2**3)
