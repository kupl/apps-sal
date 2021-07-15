a = input()
for i in range(len(a)):
    if (i + 1) % 2 == 1:
        if a[i] == "R" or a[i] == "U" or a[i] == "D":
            continue
        else:
            print("No")
            return
    else:
        if a[i] == "L" or a[i] == "U" or a[i] == "D":
            continue
        else:
            print("No")
            return
print("Yes")
