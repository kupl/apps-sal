def __starting_point():
    word = input()
    if word.startswith("CODEFORCES"):
        print("YES")
    elif word.startswith("CODEFORCE") and word.endswith("S"):
        print("YES")
    elif word.startswith("CODEFORC") and word.endswith("ES"):
        print("YES")
    elif word.startswith("CODEFOR") and word.endswith("CES"):
        print("YES")
    elif word.startswith("CODEFO") and word.endswith("RCES"):
        print("YES")
    elif word.startswith("CODEF") and word.endswith("ORCES"):
        print("YES")
    elif word.startswith("CODE") and word.endswith("FORCES"):
        print("YES")
    elif word.startswith("COD") and word.endswith("EFORCES"):
        print("YES")
    elif word.startswith("CO") and word.endswith("DEFORCES"):
        print("YES")
    elif word.startswith("C") and word.endswith("ODEFORCES"):
        print("YES")
    elif word.endswith("CODEFORCES"):
        print("YES")
    else:
        print("NO")


__starting_point()
