a = sorted(map(int, input().split()))
if (a[0] + a[1]) * 2 < a[2]:
    print(a[0] + a[1])
else:
    print(sum(a) // 3)
