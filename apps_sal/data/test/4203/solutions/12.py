s = input()
if s[0] == "A" and s[2:-1].count("C") == 1:
    c = s[2:-1].index('C')
    if (s[1] + s[2:c + 2] + s[c + 3:]).islower():
        print('AC')
    else:
        print('WA')
else:
    print('WA')
