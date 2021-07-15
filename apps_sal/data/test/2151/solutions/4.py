nQ = int(input())
for q in range(nQ):
    nD = int(input())
    ds = input()
    if nD >= 3:
        print("YES")
        print(2)
        print(ds[0], ds[1:])
    elif nD == 2 and int(ds[0]) < int(ds[1]):
        print("YES")
        print(2)
        print(ds[0], ds[1])
    else:
        print("NO")

