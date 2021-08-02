a = list(map(int, input().split()))

if a[0] % a[1] == 0:
    b = (a[0] // a[1])
else:
    b = (a[0] // a[1]) + 1
c = b * a[2]
print(c)
