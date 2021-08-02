while True:
    try:
        mp = dict()
        a = list()
        n = int(input())
        for i in range(n):
            s = input()
            num = eval(s)
            a.append(num)
            if num in mp:
                mp[num] = mp[num] + 1
            else:
                mp[num] = 1
        for i in a:
            print(mp[i], end=' ')
        print()
    except EOFError:
        break
