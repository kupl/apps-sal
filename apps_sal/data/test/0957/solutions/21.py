import sys
s = input()
a = s.find("h")
if a != -1:
    s = s[a:]
    a = s.find("e")
    if a != -1:
        s = s[a:]
        a = s.find("i")
        if a != -1:
            s = s[a:]
            a = s.find("d")
            if a != -1:
                s = s[a:]
                a = s.find("i")
                if a != -1:
                    print("YES")
                    return
print("NO")

