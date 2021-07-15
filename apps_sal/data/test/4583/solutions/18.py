a, b, c, d = list(map(int, list(input())))
if a + b + c + d == 7:
    print(("{}+{}+{}+{}=7".format(a, b, c, d)))
elif a + b + c - d == 7:
    print(("{}+{}+{}-{}=7".format(a, b, c, d)))
elif a + b - c + d == 7:
    print(("{}+{}-{}+{}=7".format(a, b, c, d)))
elif a - b + c + d == 7:
    print(("{}-{}+{}+{}=7".format(a, b, c, d)))
elif a + b - c - d == 7:
    print(("{}+{}-{}-{}=7".format(a, b, c, d)))
elif a - b - c + d == 7:
    print(("{}-{}-{}+{}=7".format(a, b, c, d)))
elif a - b + c - d == 7:
    print(("{}-{}+{}-{}=7".format(a, b, c, d)))
elif a - b - c - d == 7:
    print(("{}-{}-{}-{}=7".format(a, b, c, d)))

