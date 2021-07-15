k, a, b = [int(i) for i in input().split()]
if a % k != 0:
    a += k - a % k
if (b - a + 1) % k == 0:
    print((b-a+1)//k)
else:
    print((b-a+1)//k+1)


