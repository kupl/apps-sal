a = input()
b = input()
if len(a) > len(b):
    print("GREATER")
elif len(a) < len(b):
    print("LESS")
else:
    for i in range(len(a)):
        if a[i] > b[i]:
            print("GREATER")
            break
        elif a[i] < b[i]:
            print("LESS")
            break
    else:
        print("EQUAL")
