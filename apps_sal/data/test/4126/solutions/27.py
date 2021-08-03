def resolve():
    s = input()
    if s == s[::-1]:
        s_1 = s[:len(s) // 2]
        s_2 = s[(len(s) + 1) // 2:]
        if (s_1 == s_1[::-1]) and (s_2 == s_2[::-1]):
            print('Yes')
        else:
            print('No')
    else:
        print('No')


resolve()
