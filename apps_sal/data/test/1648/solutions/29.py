a = list(map(int,input().split()))
N = a[0]
K = a[1]

i = 2
x = (N-K+1)
y = 1
z = (x*y)%(10**9+7)
print(z)

while K >= i:
    if (N-K+1) >= i:
        x = (N-K+2-i)*x//i
        y = (K-i+1)*y//(i-1)
        z = (x*y)%(10**9+7)
        print(z)
    else:
        print((0))
    i = i + 1

