def ans():
    h, n = [int(i) for i in input().split()]
    div = 2**(h - 1)
    mystr = ""
    for i in range(h):
        if n > div:
            mystr += "G"
            div += 2**(h - i - 2)
        else:
            mystr += "L"
            div -= 2**(h - i - 2)

    if mystr[0] == "L":
        ans = 1
    elif mystr[0] == "G":
        ans = 2**h
    for i in range(len(mystr) - 1):
        if mystr[i + 1] == mystr[i]:
            ans += 2**(h - i - 1)
        else:
            ans += 1

    print(ans)

    return


ans()
