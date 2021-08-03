a = input()
b = a.split()

if b[0] == "5" and b[1] == "5" and b[2] == "7":
    print("YES")
elif b[0] == "5" and b[1] == "7" and b[2] == "5":
    print("YES")
elif b[0] == "7" and b[1] == "5" and b[2] == "5":
    print("YES")
else:
    print("NO")
