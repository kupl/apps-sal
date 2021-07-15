n = int(input())

t = input()

if t == "1":
    print((10 ** 10 * 2))
elif t == "11":
    print((10 ** 10))
else:
    if "00" in t or "111" in t or "010" in t:
        print((0))
    else:
        a = t.count("0")
        if t[-1] == "1":
            print((10 ** 10 - a))
        else:
            print((10 ** 10 - a + 1))

