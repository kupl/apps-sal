n = int(input())
a = [0] * 1010
name = 1
ser = 0
dim = 0
a = list(map(int, input().split()))
flag = 1
while n > 1:
    if name % 2 != 0:
        ser += max(a[0], a[n - 1])
        if a[0] > a[n - 1]:
            del a[0]
        else:
            del a[n - 1]
    else:
        dim += max(a[0], a[n - 1])
        if a[0] > a[n - 1]:
            del a[0]
        else:
            del a[n - 1]
    n -= 1
    name += 1
if name % 2 != 0:
    ser += a[0]
else:
    dim += a[0]
print(ser, dim)
