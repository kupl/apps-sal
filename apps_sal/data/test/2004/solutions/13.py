n = int(input())
outstr = ""
if n % 2 == 0:
    print(n // 2 * 3)
    phrasea = ""
    phraseb = ""
    for i in range(1, n // 2 + 1):
        phrasea += "{} ".format(2 * i)
        phraseb += "{} ".format(2 * i - 1)

    outstr = phrasea + phraseb + phrasea
    outstr = outstr[:-1]
    print(outstr)
else:
    print((3 * n - 1) // 2)
    phrasea = ""
    phraseb = ""
    for i in range(1, (n + 1) // 2):
        phrasea += "{} ".format(2 * i)
        phraseb += "{} ".format(2 * i - 1)
    phraseb += "{} ".format(n)

    outstr = phrasea + phraseb + phrasea
    outstr = outstr[:-1]
    print(outstr)
