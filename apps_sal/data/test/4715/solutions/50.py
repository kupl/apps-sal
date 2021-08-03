a = input().split()
if a[0] == a[1] == a[2]:
    print(1)
elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
    print(2)
else:
    print(3)
