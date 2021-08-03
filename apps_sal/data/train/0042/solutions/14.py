for _ in range(int(input())):
    s = input()
    n = len(s)
    i = 0
    j = 0
    c = 0
    ans = 0
    while(i < n):
        if(s[i] == '0'):
            c += 1
        if(s[i] == '1'):
            x = 0
            y = 0
            for j in range(i, n):
                x = x * 2
                if(s[j] == '1'):
                    x += 1
                # print(x,y,c)
                if(x - y - 1 <= c):
                    ans += 1
                    # print(i,j)
                else:
                    break
                y += 1
            c = 0
        i += 1
    print(ans)
