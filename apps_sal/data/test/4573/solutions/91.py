n = int(input())
xx = list(map(int, input().split()))
yy = sorted(xx)
a = yy[n // 2 - 1]
b = yy[n // 2]
for x in xx:
    if x <= a:
        print(b)
    elif x >= b:
        print(a)
