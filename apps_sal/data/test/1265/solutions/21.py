a = list(input())
b = list(input())

if(len(a)!=len(b)):
    print("NO")
elif len(a) == 1:
    if a == b :
        print("YES")
    else:
        print("NO")
else:
    if a == b :
        print("YES")
    elif '1' in a and '1' in b :
        print("YES")
    else:
        print("NO")

