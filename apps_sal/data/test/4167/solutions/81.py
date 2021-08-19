a = list(map(int, input().split()))
b = a[0] // a[1]
if a[1] % 2 != 0:
    print(b ** 3)
elif a[0] % a[1] >= a[1] // 2:
    print(b ** 3 + (b + 1) ** 3)
else:
    print(2 * b ** 3)
