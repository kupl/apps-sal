a = input()
b = int(input())
c = 1
if a[0] != "1":
    print(a[0])
if a[0] == "1":
    for i in range(len(a) - 1):
        if a[i] == "1" and a[i + 1] == "1":
            c = c + 1
        else:
            break
    if c >= b:
        print(1)
    else:
        print(a[c])
