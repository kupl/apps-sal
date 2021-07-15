s = input()
nota = len(s) - s.count("a")
if nota % 2 != 0:
    print(":(")
else:
    if nota == 0:
        print(s)
    elif s[-nota//2:].count("a") > 0:
        print(":(")
    else:
        s1 = s.replace("a", "")
        if s1[:nota//2] != s1[nota//2:]:
            print(":(")
        else:
            print(s[:-nota//2])
