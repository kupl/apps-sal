a = input()
b = input()
if len(a) == len(b):
    if a == b:
        print("EQUAL")
    elif a < b:
        print("LESS")
    else:
        print("GREATER")
elif len(a) < len(b):
    print("LESS")
else:
    print("GREATER")
