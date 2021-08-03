s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("NO")
    return
elif len(s1) == 1:
    if s1 != s2:
        print("NO")
    else:
        print("YES")
    return
elif s1 == s2:
    print("YES")
    return
if (s1.count("1") != 0) and (s2.count("1") != 0):
    print("YES")
else:
    print("NO")
