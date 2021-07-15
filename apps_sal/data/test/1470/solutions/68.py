x = int(input())
n = x//11
k = x%11
if k==0:
    print(2*n)
elif 1<=k<=6:
    print(2*n+1)
else:
    print(2*(n+1))
