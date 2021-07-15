n, a = int(input()), set(map(int, input().split()))
if (len(a) <3):
    print("YES")
elif len(a) == 3:
    a = sorted(list(a))
    if a[1] - a[0] == a[2] - a[1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
