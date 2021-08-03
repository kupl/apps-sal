
while(1):
    try:
        s = input()
        a = []
        for i in range(0, len(s), 2):
            a.append(int(s[i]))
        a.sort()
        for ele in a[:len(a) - 1]:
            print(ele, end='+')
        print(a[-1])
    except EOFError:
        break
