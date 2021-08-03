n, l, r = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = list()
b1 = list()
u = 1
for i in range(0, n):
    if(i >= l - 1 and i <= r - 1):
        a1.append(a[i])
        b1.append(b[i])
    else:
        if(a[i] != b[i]):
            u = 0
            break
a1.sort()
b1.sort()
if(a1 != b1 or u == 0):
    print("LIE")
else:
    print("TRUTH")
