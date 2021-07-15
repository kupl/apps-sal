def __starting_point():
    s = input()
    sa, ea, sb, eb, sc, ec = 0, 0, 0, 0, 0, 0
    for i in range(len(s)):
        if(s[i] == 'a'):
            if(sa == 0):
                sa, ea = i+1, i+1
            else:
                ea = i+1
        if(s[i] == 'b'):
            if(sb == 0):
                sb, eb = i+1, i+1
            else:
                eb = i+1
        if(s[i] == 'c'):
            if(sc == 0):
                sc, ec = i+1, i+1
            else:
                ec = i+1
    max_diff = 0
    if(sa != 0):
        if(sb != 0):
            max_diff = max(max_diff, abs(eb-sa), abs(ea-sb))
        if(sc != 0):
            max_diff = max(max_diff, abs(ec-sa), abs(ea-sc))
    if(sb != 0):
        if(sc != 0):
            max_diff = max(max_diff, abs(ec-sb), abs(eb-sc))
    print(max_diff)
__starting_point()
