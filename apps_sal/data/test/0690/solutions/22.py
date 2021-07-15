n = input()[::-1]
res = ""
for i in n:
    i = int(i)
    if i < 5:
        res += "O-|"
        res += "O" * i + "-" + "O" * (4 - i)
    else:
        res += "-O|"
        res += "O" * (i - 5) + "-" + "O" * (9 - i)
    print(res)
    res = ""

