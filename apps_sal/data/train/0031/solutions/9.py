for __ in range(int(input())):
    s = input()
    x = 0
    y = 0
    ans = 0
    d = {}
    for i in range(len(s)):
        if(s[i] == 'N'):
            if(d.get((x, y, x, y + 1)) == None):
                ans += 5
                d[(x, y, x, y + 1)] = 1
                d[(x, y + 1, x, y)] = 1
            else:
                ans += 1
            y = y + 1
        elif(s[i] == 'S'):
            if(d.get((x, y, x, y - 1)) == None):
                ans += 5
                d[(x, y, x, y - 1)] = 1
                d[(x, y - 1, x, y)] = 1
            else:
                ans += 1
            y = y - 1
        elif(s[i] == 'W'):
            if(d.get((x, y, x - 1, y)) == None):
                ans += 5
                d[(x, y, x - 1, y)] = 1
                d[(x - 1, y, x, y)] = 1
            else:
                ans += 1
            x = x - 1
        else:
            if(d.get((x, y, x + 1, y)) == None):
                ans += 5
                d[(x, y, x + 1, y)] = 1
                d[(x + 1, y, x, y)] = 1
            else:
                ans += 1
            x = x + 1
    print(ans)
