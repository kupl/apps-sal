def code_parsing(string):
    string = ''.join(sorted(string))

    x = string.count("x")
    y = string.count("y")

    if x > y:
        return "x" * (x - y)
    elif x < y:
        return "y" * (y - x)
    else:
        return ""

s = input()
print(code_parsing(s))


