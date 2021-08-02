a = sorted(list(map(int, input().split())))
if a[0] == a[1]:
    print(a[0] + a[1])
else:
    print(a[1] * 2 - 1)
