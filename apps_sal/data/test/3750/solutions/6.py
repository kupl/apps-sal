k, a, b = input().split()
k = int(k)
a = int(a)
b = int(b)
if a+b < k:
    print(-1)
else:
    if ((a%k > 0 and b//k > 0) or (a%k == 0)) and \
        ((b%k > 0 and a//k > 0) or (b%k == 0)):
        print(a//k + b//k)
    else:
        print(-1)
