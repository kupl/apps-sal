a = list(map(int, input().split()))
if len(a) < 5:
    print(0)
else:
    print(min(a[0], a[1], a[2] // 2, a[3] // 7, a[4] // 4))
