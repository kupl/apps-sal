s = input().split()
a = int(s[0])
b = int(s[1])

i = 1
while i:
    if i % 2 > 0:
        if a < i:
            print("Vladik")
            break
        else:
            a -= i
    else:
        if b < i:
            print("Valera")
            break
        else:
            b -= i
    i += 1
