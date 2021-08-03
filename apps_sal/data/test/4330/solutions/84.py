a = list(map(int, input().split()))
if (a[0] + a[1]) % 2 == 0:
    print((a[0] + a[1]) // 2)
else:
    print("IMPOSSIBLE")
