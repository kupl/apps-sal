a = list(map(int, input().split()))
if a[0] + a[3] == a[1] + a[2] or a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or 2 * a[0] == sum(a) or 2 * a[1] == sum(a) or 2 * a[2] == sum(a) or a[3] * 2 == sum(a):
    print("Yes")
else:
    print("No")
