def getints(str):
    return list(map(int, str.split(" ")))


a = getints(input())

if a[1] - a[0] == a[2] - a[1] == a[3] - a[2]:
    print(2 * a[3] - a[2])
elif (0 not in a) and (a[1] / a[0] == a[2] / a[1] == a[3] / a[2]):
    if (a[3] * a[3] % a[2]) == 0:
        print(a[3] * a[3] // a[2])
    else:
        print(42)
else:
    print(42)
