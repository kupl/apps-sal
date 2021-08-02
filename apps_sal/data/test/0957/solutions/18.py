a = str(input(""))
length = len(a)
# print(a.find("h"))
if a.find("h") != -1:
    a = a[(a.find("h") + 1):]
    # print(a)
    if a.find("e") != -1:
        a = a[(a.find("e") + 1):]
        # print(a)
        if a.find("i") != -1:
            a = a[(a.find("i") + 1):]
            # print(a)
            if a.find("d") != -1:
                a = a[(a.find("d") + 1):]
                # print(a)
                if a.find("i") != -1:
                    print("YES")
                    return
                else:
                    print("NO")
                    return
            else:
                print("NO")
                return
        else:
            print("NO")
            return
    else:
        print("NO")
        return
else:
    print("NO")
    return
