n = int(input())
a = list(map(lambda a: (-int(a) - 1 if int(a) >= 0 else int(a)), input().split()))

b = 1
for val in a:
    if val < 0:
        b *= -1

if b < 0:
    i_max = 0
    for i in range(n):
        if abs(a[i_max]) < abs(a[i]):
            i_max = i
    a[i_max] =  -a[i_max] - 1

print(" ".join(map(str, a)))
