arr = []
for _ in range(int(input())):
    arr.append(int(input()))
arr2 = arr.copy()
arr2.sort()
z = arr2[-1]
zz = arr2[-2]
for k in arr:
    if k != z:
        print(z)
    else:
        print(zz)
