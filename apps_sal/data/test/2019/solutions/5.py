for _ in range(int(input())):
    s = input()
    o = 0
    z = 0
    for i in range(len(s)):
        if s[i] == '0':
            z += 1
        else:
            o += 1
    if min(o, z) % 2 == 1:
        print('DA')
    else:
        print('NET')
