s = input()
if s[0] == '-':
    if s[-1] >= s[-2]:
        if s[:-1] != '-0':
            print(s[:-1])
        else:
            print(0)
    elif s[:-2] + s[-1] != '-0':
        print(s[:-2] + s[-1])
    else:
        print(0)
else:
    print(s)
