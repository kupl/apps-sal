a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

if not((a[0][2] - a[0][1]) == (a[1][2] - a[1][1]) == (a[2][2] - a[2][1])):
    print("No")
    return

if not((a[0][1] - a[0][0]) == (a[1][1] - a[1][0]) == (a[2][1] - a[2][0])):
    print("No")
    return

if not((a[0][0] - a[1][0]) == (a[0][1] - a[1][1]) == (a[0][2] - a[1][2])):
    print("No")
    return

if not((a[2][0] - a[1][0]) == (a[2][1] - a[1][1]) == (a[2][2] - a[1][2])):
    print("No")
    return
print("Yes")
