n = int(input())
L = list(map(int, input().split()))
ma = L.index(n)
mi = L.index(1)
if n == 2:
    print(1)
else:
    print(n-1-min(ma,mi,n-1-ma,n-1-mi))

